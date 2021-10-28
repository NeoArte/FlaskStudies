from flask import Flask, request, render_template

# Create our app -------------------
app = Flask(__name__)

# Content of our app -------------------

@app.route("/", methods=['GET', 'POST'])
def index():
    weight = ''
    height = ''

    # BMI is measured in Kg/M², the equation for it is Mass / Height^2
    if request.method == "POST":

        # We must verify if somehow the user sent a field with no value ("") and if that is the case counter it.
        if weight == '' or height == '':
            print('weight: ', weight=='')
            print('height: ', height=='')
            return render_template('index.html',
                                    missing_weight=weight == '',
                                    missing_height=height == '')

        weight = float(request.form.get('weight'))
        height = int(request.form.get('height'))
        bmi = weight / (height**2)
    
    return render_template('index.html')

# Running our app -------------------

app.run()