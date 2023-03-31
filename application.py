from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

resultsOfAsk = [1,500,500,500,500,500] #list of results of ask

#TO DO
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

#SOME TO DO
@app.route('/ask', methods=['GET'])
def ask():
    return render_template('ask.html')

#TO DO
@app.route('/results', methods=['GET'])
def results():
    if request.method == 'GET':
        return render_template('results.html', resultsOfAsk=resultsOfAsk)
    else:
        return render_template('ask.html')

#TO DO
@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)