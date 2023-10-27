from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/query_results')
def query_results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run()
