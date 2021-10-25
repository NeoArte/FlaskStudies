from flask import Flask


# --- --- --- --- --- ---  Create our flask app --- --- --- --- --- --- 

app = Flask(__name__)

# Flask(__name__) will print ("<Flask 'app'>"), 'app' here refers to the file (app.py) and not the variable name (app)
# print(app) --> <Flask 'app'>"
# print(__name__) --> __main__
# print(Flask(__name__)) --> <Flask 'app'>"

# --- --- --- --- --- --- Defines what happens on the flask app --- --- --- --- --- --- 

# GET requests like these (that makes the pages actually be acessed) are handled by Flask
@app.route('/') # app.route sets the route at which the funciont reffers to (like the urlpattern in Django that defines a url and a views function)
def welcome():
    return home() # If we return another function and not text, we can make the action of redirecting the users (apparently)

@app.route('/home')
def home():
    return 'This is my first flask app! <3 You were redirect from the url /'

@app.route('/users')
def users():
    return 'Here you can find all of our user database! :D'

# --- --- --- --- --- --- Run the flask app --- --- --- --- --- --- 

app.run() # Runs our flask app