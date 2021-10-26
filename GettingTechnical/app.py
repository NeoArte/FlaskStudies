from flask import Flask, request

# Setup for the app ======= o ======= o ======= o =======
app = Flask(__name__)


# Defining what happens on the app ======= o ======= o ======= o =======

@app.route('/')
def index():
    return "That is our first page! Welcome!"

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