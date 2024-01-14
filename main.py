from flask import Flask, render_template, g, request

from HeaderDataBase import HeaderDB
from ValidationPostForm import validation_form

import sqlite3
import os


DATA_BASE = 'data_base.db'
DEBUG = True
SECRET_KEY = '565ca975e16072ef18737e125e51702c8c24a209'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATA_BASE=os.path.join(app.root_path, 'data_base.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATA_BASE'])
    con.row_factory = sqlite3.Row
    return con


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_connect_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/', methods=['POST', 'GET'])
def main():
    db = get_db()
    dbase = HeaderDB(db)
    if request.method == 'POST':
        validation_form()
        return render_template('index.html', title='Главная', head_menu=dbase.get_menu())
    return render_template('index.html', title='Главная', head_menu=dbase.get_menu())


@app.route('/catalog', methods=['POST', 'GET'])
def catalog():
    db = get_db()
    dbase = HeaderDB(db)
    return render_template('catalog.html', title='Каталог',
                           head_menu=dbase.get_menu(), cards=dbase.get_card_anons())


@app.route('/about')
def about():
    db = get_db()
    dbase = HeaderDB(db)
    return render_template('about.html', title='О нас', head_menu=dbase.get_menu())


@app.route('/signin')
def signin():
    return render_template('signin.html', title='Войти', head_menu=[])


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    db = get_db()
    dbase = HeaderDB(db)

    if request.method == 'POST':
        if len(request.form['images']) > 4 and len(request.form['name']) > 4:
            res = dbase.add_admin_card(
                request.form['images'], request.form['name'], request.form['title'], request.form['price'])
            if not res:
                return False
            return True
    return render_template('admin.html', title='Панель администратора', head_menu=dbase.get_menu())


@app.errorhandler(404)
def not_found(error):
    return render_template('notFound.html', title='Страница не найдена', head_menu=[])


if __name__ == '__main__':
    app.run(debug=True)
