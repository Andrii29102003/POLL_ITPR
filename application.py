from flask import Flask
from flask import request
from flask import render_template
import random 
from loader import dblite



app = Flask(__name__)

resultsOfAsk = [1, 500, 500, 500, 500, 500] # list of results of ask
          

# //--TO DO
# //-- VlaGan: перші тестові накидки (поки онлі коннект до аска)
@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        request_values = [request.values["username"], request.values["ask_id"]]
        print("REQUEST VALUES =", request_values)
        #return render_template("create.html", args=request_values)

    print("--rendering index/default page")
    return render_template("index.html")


# SOME TO DO
@app.route('/ask', methods=['GET'])
def ask():
    """TESTING"""    
    #urls = ['https://assets.aboutamazon.com/dims4/default/42868bd/2147483647/strip/true/crop/1279x720+0+0/resize/1320x743!/format/webp/quality/90/?url=https%3A%2F%2Famazon-blogs-brightspot.s3.amazonaws.com%2F06%2Ff1%2F8767bdab489e8e2780a3f870e8c5%2Falexa-for-pets-1.jpg', "https://assets.aboutamazon.com/dims4/default/42868bd/2147483647/strip/true/crop/1279x720+0+0/resize/1320x743!/format/webp/quality/90/?url=https%3A%2F%2Famazon-blogs-brightspot.s3.amazonaws.com%2F06%2Ff1%2F8767bdab489e8e2780a3f870e8c5%2Falexa-for-pets-1.jpg", "https://npr.brightspotcdn.com/dims4/default/4c6a59a/2147483647/strip/true/crop/4032x2268+0+378/resize/1200x675!/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Flegacy%2Fsites%2Fwxxi%2Ffiles%2F202004%2Fsassy_sick.jpg"]
    return render_template('ask.html')

# def ask():
#     return render_template('ask.html')


# TO DO
@app.route('/results', methods=['GET'])
def results():
    if request.method == 'GET':
        return render_template('results.html', resultsOfAsk=resultsOfAsk)
    else:
        return render_template('ask.html')


# TO DO
@app.route('/create', methods=['GET'])
def create():
    passw="I love to **********************"
    #id=dblite.new(passw=passw)
    id=len(dblite.get_all_pools()) + 1
    
    return render_template('create.html', id=id, passw=passw)


@app.route('/submit_form/<int:id>/<string:passw>', methods=['GET'])
def submit_form(id, passw):
    print('resv ', id, passw)
    link1 = request.args.get('link1')
    link2 = request.args.get('link2')
    link3 = request.args.get('link3')
    link4 = request.args.get('link4')
    link5 = request.args.get('link5')

    dblite.add_new_poll(passw,[link1,link2,link3,link4,link5], )

    return 'Form submitted successfully!'


if __name__ == '__main__':
    app.run(debug=True)
