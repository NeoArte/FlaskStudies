from flask import Flask, request, render_template

# Create our app -------------------
app = Flask(__name__)

# Content of our app -------------------

@app.route("/", methods=['GET', 'POST'])
def index():
    # BMI is measured in Kg/M², the equation for it is Mass / Height^2
    if request.method == "POST":
        mass = request.form.get('mass')
        height = request.form.get('height')
        print(mass, ':', type(mass))
        #bmi = mass / (height**2)
    
    return render_template('index.html')

# Running our app -------------------

app.run()