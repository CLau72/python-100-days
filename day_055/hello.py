from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def inner():
        return f"<strong>{function()}</strong>"
    return inner


def make_emphasis(function):
    def inner():
        return f"<em>{function()}</em>"
    return inner


def make_underlined(function):
    def inner():
        return f"<u>{function()}<u>"
    return inner

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgifimage.net%2Fwp-content%2Fuploads%2F2017%2F10%2Fhead-explode-gif-tim-and-eric-6.gif&f=1&nofb=1">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_goodbye():
    return 'Later,nerd'

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name.title()}! Here is your number {number}"

if __name__ == "__main__":
    app.run(debug=True)