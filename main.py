from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
     context = {
         "caption": "Главная страница",
         "page1": " active",
         "page2": " ",
         "page3": " "
     }
     return render_template('index.html', **context)


@app.route('/blog')
def blog():
    context = {
        "caption": "Cтраница блога",
        "page1": " ",
        "page2": " active",
        "page3": " "
    }
    return render_template('blog.html', **context)

@app.route('/contacts')
def contacts():
    context = {
        "caption": "Страница контактов",
        "page1": " ",
        "page2": " ",
        "page3": " active"
    }
    return render_template('contacts.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
