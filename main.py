from flask import Flask, render_template

app = Flask(__name__)

head_menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'Каталог', 'url': 'catalog'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Контакты', 'url': 'contacts'}
]


@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html', title='Главная', head_menu=head_menu)


@app.route('/catalog')
def catalog():
    return render_template('catalog.html', title='Каталог', head_menu=head_menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О нас', head_menu=head_menu)


if __name__ == '__main__':
    app.run(debug=True)
