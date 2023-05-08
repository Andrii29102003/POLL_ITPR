from flask import Flask, g
from flask import request
from flask import render_template
from flask import session
#import matplotlib.pyplot as plt
import random 
from dblite import DB
from collections import Counter
from dblite import new_poll_query, create_db_tables, get_link_by_passw, save_poll_result, get_poll_answ
from side_func import * 
import json
import time

app = Flask(__name__)
app.secret_key = 'KaixenixTOP'
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
    #result = db.execute_query("SELECT * FROM ask")
    #print('result: ', result)
    #urls = ['https://assets.aboutamazon.com/dims4/default/42868bd/2147483647/strip/true/crop/1279x720+0+0/resize/1320x743!/format/webp/quality/90/?url=https%3A%2F%2Famazon-blogs-brightspot.s3.amazonaws.com%2F06%2Ff1%2F8767bdab489e8e2780a3f870e8c5%2Falexa-for-pets-1.jpg', "https://assets.aboutamazon.com/dims4/default/42868bd/2147483647/strip/true/crop/1279x720+0+0/resize/1320x743!/format/webp/quality/90/?url=https%3A%2F%2Famazon-blogs-brightspot.s3.amazonaws.com%2F06%2Ff1%2F8767bdab489e8e2780a3f870e8c5%2Falexa-for-pets-1.jpg", "https://npr.brightspotcdn.com/dims4/default/4c6a59a/2147483647/strip/true/crop/4032x2268+0+378/resize/1200x675!/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Flegacy%2Fsites%2Fwxxi%2Ffiles%2F202004%2Fsassy_sick.jpg"]
    return render_template('ask.html')

# def ask():
#     return render_template('ask.html')




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
        links = 5 
        str_links = ['link' + str(i) for i in range(1, links+1)]
        url_links = [request.values[str_link] for str_link in str_links]
        
        print(url_links)
        db.execute_query(new_poll_query, (passw, del_passw, json.dumps(url_links)))
        return render_template("index.html")
    
    return render_template('create.html', id=id, passw=passw, del_passw=del_passw)

@app.route('/results/<people_name>', methods=["GET", 'POST'])
def results(people_name):
    if request.method == 'GET': 
        pass
        # return render_template("index.html")


    print('name ', people_name)
    # Get the values of the input ranges from the form
    input_values =  []
    #cab  pass how many links
    for url in range(2,7):
        input_name = 'volume' + str(url)
        input_value = request.form.get(input_name)
        input_values.append(input_value)
    db = get_db()
    passw = session.get(people_name)
    try: 
        db.execute_query(save_poll_result,(passw, people_name, json.dumps(input_values)))
        time_answ_save = time.time()
    except: 
        pass
        # return 'Ваша відповідь уже записана' #TO DO добавити сторінку де можна буде перейти зразу до результатів
    
    result = db.execute_query(get_poll_answ,(passw,))
    print(result)
    
    scores = {}
    for i in range(len(json.loads(result[0][1]))):
        i = i+1
        scores[i] = []
        for j, data in enumerate(result):
            lst = json.loads(data[1])
            scores[i].append(int(lst[i-1]))
        scores[i] = sorted(scores[i])
    
    scores_counted = {}      
    for key, values in scores.items():
        scores_counted[key] = dict(Counter(values))

            
    print(scores_counted)
    passed_poll_times = len(result)
    
    result = db.execute_query(get_link_by_passw,(passw,))
    print(result, type(result))
    
    try: 
        urls = json.loads(result[0][0])
    except: 
        return f'Немає такого опитування як {passw}, перевірте коректність, або Адміністратор вже видалив його'

    count=0
    sum_a=0
    avgMark=[]
    for key, value in scores_counted.items():
        for key, mark in value.items():
            sum_a+=key*mark
            count+=mark
            avgMark.append(round(sum_a/count, 1))
    
    print(avgMark)#DEL
    print(scores_counted)
    # data = scores_counted
    percentages_data = {}
    for key, inner_data in scores_counted.items():
        total_sum = sum(inner_data.values())
        percentages = {inner_key: int((value / total_sum) * 100) for inner_key, value in inner_data.items()}
        percentages_data[key] = percentages

    print(percentages_data)
    #return render_template('results_cool.html', data=scores_counted, passed_poll_times= passed_poll_times)
    return render_template('test_results.html', data=scores_counted, passed_poll_times= passed_poll_times, urls= urls, avgMark=avgMark, percentages_data = percentages_data)

    # if request.method == 'GET':
    #     return render_template('results.html', resultsOfAsk=1)
    # else:
    #     return render_template('ask.html')

# @app.route('/submit_form/<int:id>/<string:passw>', methods=['GET']) # DO NOT USE
# def submit_form(id, passw):
#     print('resv ', id, passw)


#     # dblite.add_new_poll(passw,[link1,link2,link3,link4,link5], )

#     return 'Form submitted successfully!'


@app.route('/take_poll', methods=['POST'])
def process_form():
    # Form processing logic here
    people_name = request.form.get('username')
    poll_passw = request.form.get('ask_id')
    session[people_name] = poll_passw
    print('passw', poll_passw)
    db = get_db()
    result = db.execute_query(get_link_by_passw,(poll_passw,))
    print(result, type(result))
    
    try: 
        urls = json.loads(result[0][0])
    except: 
        return f'Немає такого опитування як {poll_passw}, перевірте коректність, або Адміністратор вже видалив його'

    return render_template('ask_dinamic.html', people_name = people_name, urls=urls)


#TEST
@app.route('/test_ask', methods=['GET'])
def test_ask():
    pass
#####





if __name__ == '__main__':
    app.run(debug=True, port=5001)