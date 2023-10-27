from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/query_results')
def query_results():
    query = request.args.get('query')
    return render_template('results.html', search_query=query)


if __name__ == '__main__':
    app.run()
