from flask import Flask
from flask import request
from flask import render_template
#from db import db



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
    urls = ['https://assets.aboutamazon.com/dims4/default/42868bd/2147483647/strip/true/crop/1279x720+0+0/resize/1320x743!/format/webp/quality/90/?url=https%3A%2F%2Famazon-blogs-brightspot.s3.amazonaws.com%2F06%2Ff1%2F8767bdab489e8e2780a3f870e8c5%2Falexa-for-pets-1.jpg', "https://assets.aboutamazon.com/dims4/default/42868bd/2147483647/strip/true/crop/1279x720+0+0/resize/1320x743!/format/webp/quality/90/?url=https%3A%2F%2Famazon-blogs-brightspot.s3.amazonaws.com%2F06%2Ff1%2F8767bdab489e8e2780a3f870e8c5%2Falexa-for-pets-1.jpg", "https://npr.brightspotcdn.com/dims4/default/4c6a59a/2147483647/strip/true/crop/4032x2268+0+378/resize/1200x675!/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Flegacy%2Fsites%2Fwxxi%2Ffiles%2F202004%2Fsassy_sick.jpg"]
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