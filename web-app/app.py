from flask import Flask, request, render_template
from backbone.search import perform_query
from backbone.fetching import fetch_speech

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/query_results')
def query_results():
    query = request.args.get('query')
    query_results = perform_query(query)
    return render_template('results.html', search_query=query, search_results=query_results)


@app.route('/show_speech/<int:result_id>')
def show_speech(result_id):
    result = fetch_speech(result_id)
    return render_template('speech.html', result=result)


if __name__ == '__main__':
    app.run()
