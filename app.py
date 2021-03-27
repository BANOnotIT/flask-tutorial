from functools import wraps
from flask import Flask, request, render_template, jsonify, Response
import pandas as pd

books = pd.read_csv('books.csv')
app = Flask(__name__)


def linkify(books):
    books['Link'] = '/isbn/' + books.index.map(str)


linkify(books)


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not request.authorization or request.authorization.username != 'librarian':
            return 'You are not allowed to do this', 401
        return func(*args, **kwargs)

    return decorated_view


def get_index():
    return books['Author'].astype(str).str[0].str.upper().sort_values().unique().tolist()


@app.route('/')
def hello():
    return render_template('index.html', name=request.args.get('name', 'world'))


@app.route('/index/')
def indx():
    return jsonify(get_index())


@app.route('/index/<symbol>/')
def indx_author(symbol):
    selected_books = books[books['Author'].astype(str).str.startswith(symbol)]
    simple_book = selected_books[['Author', 'Title', 'Genre', 'Link']]
    return Response(simple_book.to_json(orient='records'), mimetype='application/json')


@app.route('/isbn/<int:idx>', methods=['GET'])
def isbn(idx):
    if 'text/html' in request.accept_mimetypes:
        return render_template('book.html', book=books.loc[idx], pd=pd)
    return Response(books.loc[idx].to_json(), mimetype='application/json')


@app.route('/isbn/', methods=['POST'])
@login_required
def create_book():
    global books
    js = request.get_json()
    book = {
        'Author': js.get('Author'),
        'Title': js.get('Title'),
        'Genre': js.get('Genre'),
        'Height': js.get('Height'),
        'Publisher': js.get('Publisher'),
    }
    books = books.append(book, ignore_index=True)
    linkify(books)
    idx = books.tail(1).index[0]
    return isbn(idx)
