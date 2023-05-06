from flask import Flask, g
from flask import request
from flask import render_template
import random 
from dblite import DB
from dblite import new_poll_query, create_db_tables, get_link_by_passw
from side_func import * 
import json
app = Flask(__name__)
file = "data.db"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = DB(file_name=file)
        db.connect()
    return db




@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# //--TO DO
# //-- VlaGan: перші тестові накидки (поки онлі коннект до аска)
@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    db = get_db()
    _ = [db.execute_query(query) for query in create_db_tables]
    
    if request.method == "POST":
        request_values = [request.values["username"], request.values["ask_id"]]
        print("REQUEST VALUES =", request_values)
        #return render_template("create.html", args=request_values)

    print("--rendering index/default page")
    return render_template("index.html")


# SOME TO DO
@app.route('/ask_dinamic', methods=['GET'])
def ask():
    """TESTING"""    
    db = get_db()
    result = db.execute_query("SELECT * FROM ask")
    print('result: ', result)
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
@app.route('/create', methods=['POST', 'GET'])
def create():
    passw = generate_password(10)
    del_passw=str(random.randint(11111, 999999))
    #id=dblite.new(passw=passw)
    db = get_db()
    # result = db.execute_query("SELECT * FROM poll_data")
    id=len(db.execute_query("SELECT * FROM poll_data")) + 1
    if request.method == "POST":
        link1 = request.values["link1"]
        link2 = request.values["link2"]
        link3 = request.values["link3"]
        link4 = request.values["link4"]
        link5 = request.values["link5"] 
        dblite.add_new_poll(id, passw, [link1,link2,link3,link4,link5], [0,0,0,0,0], "")
        return render_template("index.html")
    
    return render_template('create.html', id=id, passw=passw, del_passw=del_passw)


@app.route('/submit_form/<int:id>/<string:passw>', methods=['GET']) # DO NOT USE
def submit_form(id, passw):
    print('resv ', id, passw)
    link1 = request.args.get('link1')
    link2 = request.args.get('link2')
    link3 = request.args.get('link3')
    link4 = request.args.get('link4')
    link5 = request.args.get('link5')

    dblite.add_new_poll(passw,[link1,link2,link3,link4,link5], )

    return 'Form submitted successfully!'


@app.route('/take_poll', methods=['POST'])
def process_form():
    # Form processing logic here
    people_name = request.form.get('username')
    poll_passw = request.form.get('ask_id')
    print('passw', poll_passw)
    db = get_db()
    result = db.execute_query(get_link_by_passw,(poll_passw,))
    print(result, type(result))
    
    
    return render_template('ask_dinamic.html', urls=json.loads(result[0][0]))

if __name__ == '__main__':
    app.run(debug=True)
