from flask import Flask

app = Flask(__name__)

@app.route('/resume')
def index():
    return "hello world, index"

@app.route('/mike')
def index():
    return "hello world, mike"


if __name__ == '__main__':
    app.run(debug=True)


