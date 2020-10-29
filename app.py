from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    # users_animal = 'lion'
    return f'Wow, {users_animal} is my favorite animal, too!'


if __name__ == '__main__':
    app.run(debug=True)
