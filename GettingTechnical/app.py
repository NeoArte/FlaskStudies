from flask import Flask, request, render_template

# Setup for the app ======= o ======= o ======= o =======
app = Flask(__name__)


# Defining what happens on the app ======= o ======= o ======= o =======

@app.route('/')
def index():
    return render_template("index.html") # Flask looks for the 'template' folder and then renders the 'index.html' file found there

@app.route('/login')
def login():
    return 'Here you can login into your account! :D'

@app.route('/authenticate', methods=['POST'])
def authenticate():
    return index()

@app.route('/register')
def register():
    return 'Here you can CREATE your own account! :0'

@app.route('/create_account', methods=['POST'])
def create_account():
    return index() #It does not change the URL when redirecting, so maybe that is not the correct way to do it (or it is! yet to discover the truth)

# Running the app ======= o ======= o ======= o =======

app.run()