from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    # users_animal = 'lion'
    return f'Wow, {users_animal} is my favorite animal, too!'


@app.route('/dessert/<users_dessert>')
def favorite_desserts(users_dessert):
    return f'Wow how did you know i like {users_dessert}'


@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    return f'{noun} is {adjective}!'


@app.route('/multiply/<number1>/<number2>')
def multiple(num1, num2):
    int(num1) * int(num2):

    return f'{int((num1)}*{num2} is'


if __name__ == '__main__':
    app.run(debug=True)
