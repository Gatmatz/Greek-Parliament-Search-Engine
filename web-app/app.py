from flask import Flask, request, render_template
from engine.TF_IDF import search


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/query_results')
def query_results():
    query = request.args.get('query')
    query_results = search(query)
    return render_template('results.html', search_query=query, search_results=query_results)


if __name__ == '__main__':
    app.run()
