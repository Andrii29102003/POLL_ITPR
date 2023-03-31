from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

#TO DO
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#SOME TO DO
@app.route('/ask', methods=['GET'])
def index():
    return render_template('index.html')

#TO DO
@app.route('/results', methods=['GET'])
def index():
    return render_template('index.html')

#TO DO
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)