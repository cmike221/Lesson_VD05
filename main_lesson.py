from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    context = {
        "caption": "Главная страница",
        "message": "Добро пожаловать на главную страницу",
        # "user": "Миша"
        "number": 5,
        "list": ["Миша", "Ксюша", "Наташа"]
    }
    return render_template('index.html', **context)
    # return render_template('shablon_for.html', **context)

@app.route('/shablon')
def index2():
    context = {
        "caption": "Вторая страница",
        "message": "Добро пожаловать на резервную страницу",
        "user": "Миша"
    }
    return render_template('index.html',  **context)
    # return render_template('shablon_for.html', **context)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
