import json
from src import main
from src import gtts

TESTING = False
if TESTING:
    from src import mock as backend
else:
    import script as backend

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = r"-sadfji3_dsfjjn"

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/create/', methods=('GET', 'POST'))
def create():
    print(request.form)
    if request.method == 'POST':
        name = request.form['name'].lower().strip()
        if not name:
            flash('name is required!')
        elif main.user_exists(name):
            flash('name has already been taken!')
        else:
            main.make_new_user(request.form)
            return redirect(url_for('use', name=name))

    return render_template('create.html')

@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        name = request.form['name'].lower()
        if not name:
            flash('Name is required!')
        elif main.user_exists(name):
            return redirect(url_for('use', name=name))
        else:
            flash('Name does not exist.')

    return render_template("login.html")

last_msg:str = ""


@app.route("/use")
def use():
    if not "name" in request.args:
        return "bad request, missing name"

    name = request.args['name']

    return render_template("use.html", name = name)

@app.route('/handle_prompt')
def handle_prompt():
    global last_msg

    if not "data" in request.args:
        return "bad request, missing data"

    prompt = request.args["data"]

    if prompt == "END":
        return main.parse_respone(backend.end("End conversation", request.args['name']))
    if prompt == "GRAPH":
        return main.parse_respone(backend.end("graph", request.args['name']))

    print(f"sending prompt: {prompt}")
    respone = backend.chat_with_gpt(prompt)
    last_msg = respone
    return main.parse_respone(respone)

@app.route('/handle_innit')
def call_back_innit():
    global last_msg

    if not "name" in request.args:
        return "bad request, missing name"

    name = request.args['name']

    print(f"sending innit")
    respone = backend.init(name)
    last_msg = respone
    return main.parse_respone(respone)

@app.route('/handle_tts')
def handle_tts():
    if not "name" in request.args:
        return "bad request, missing data"

    f = open("users/" + request.args['name'] + "/usrdata.json", "r")
    lang = json.load(f)["user_information"]["personal_information"]["language_choice"]


    speak = backend.getTTSString(last_msg)
    gender = "male"
    print("\n ======= in to tts\n", lang, gender, speak)
    tts = gtts.synthesise(speak, lang, gender)
    return "done"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port = 8080, debug=True)
