# Flask starter app

## Install Python
You'll need python. Version >=3.6 prefered.

For Windows you can install from [official release](https://www.python.org/downloads/windows/). 
Do NOT forget to enable *pip* on installation.

On Mac OS you jave python 2.7 preinstalled. I'd recommend install the latest version [using brew](https://brew.sh/).

On Linux you have required version under the `python3` command.

Check the installation with this commands:
```bash
python --version  # or python3 --version           
# Python 3.6.9

pip --version  # or pip3 --version
# pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
```

## Install Packages

Once you've installed Python you have *pip* already. On Linux and Mac OS it can be under `pip3` command.

To install packages run:

```bash
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
```

This command installs Flask and Pandas. The latter is needed for CSV manipulation.

## Data

https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/c05e98672b8d52fa0cb94aad80f75eb78342e5d4/books.csv

## Links
- https://flask.palletsprojects.com ― Official Flask documentation. If you have any questions they are likely to be solved and documented there.
- http://gg.gg/mega-fask-ru [rus] ― Study book on Flask. You can learn how to use SQLAlchemy, migrations, normal Authorization and many more things from this book.
- https://fastapi.tiangolo.com/ ― Sofisticated framework which can make Swagger docs, form validation and has an advanced Dependency Injection mechanisms.
