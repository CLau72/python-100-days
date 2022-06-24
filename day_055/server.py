from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0,9)

@app.route('/')
def game_prompt():
    return "<h1>Guess a Number Between 0 and 9</h1>" \
           "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"


@app.route('/<int:guessed_number>')
def guessed_number(guessed_number):
    if guessed_number == random_number:
        return '<h1 style="color: green">You Win!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif guessed_number > random_number:
        return '<h1 style="color: purple">Too High ⬆️</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guessed_number < random_number:
        return '<h1 style="color: red">Too Low ⬇️</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

if __name__ == "__main__":
    app.run()