from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/query-results')
def query_results():
    return 'Query results'


if __name__ == '__main__':
    app.run()
