from flask import Flask
from flask import request
from flask import render_template
import sqlite3


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
    """TESTING"""    
    urls = ['https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.aboutamazon.com%2Fnews%2Fdevices%2Falexa-can-help-everyone-even-cats&psig=AOvVaw2P_7qecebHzHa_fing3BrT&ust=1680849860375000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLCUxenTlP4CFQAAAAAdAAAAABAE', "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.denver7.com%2Fnews%2Fnational%2Fnew-study-finds-humans-can-communicate-with-cats-by-blinking-slowly&psig=AOvVaw2P_7qecebHzHa_fing3BrT&ust=1680849860375000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLCUxenTlP4CFQAAAAAdAAAAABAJ", "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.denver7.com%2Fnews%2Fnational%2Fnew-study-finds-humans-can-communicate-with-cats-by-blinking-slowly&psig=AOvVaw2P_7qecebHzHa_fing3BrT&ust=1680849860375000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLCUxenTlP4CFQAAAAAdAAAAABAJ"]
    return render_template('ask_dinamic.html', urls=urls)

# def ask():
#     return render_template('ask.html')

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