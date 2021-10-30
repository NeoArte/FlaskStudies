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

        weight = request.form.get('weight')
        height = request.form.get('height')

        # We must verify if somehow the user sent a field with no value ("") and if that is the case counter it.
        if weight == '' or height == '':
            print('weight: ', weight=='')
            print('height: ', height=='')
            return render_template('index.html',
                                    missing_weight=weight == '',
                                    missing_height=height == '',
                                    result_available=False)

        weight = float(weight)
        height = int(height)/100
        bmi = weight / (height**2)
        bmi_level = "blue" # Severe Thinness & Moderate Thinness > blue | Mild Thinness & Normal > green |
                           # Overweight & Obese I > yellow | Obese II & Obese III > red
        bmi_explanation = \
            '''
            
            '''

        if bmi <= 25 and bmi > 17:
            bmi_level = 'green'
        elif bmi <= 35 and bmi > 25:
            bmi_level = 'yellow'
        elif bmi > 35:
            bmi_level = 'red'
        

        return render_template('index.html', bmi=f"{bmi:.2f}", level=bmi_level, result_available=True)
    
    return render_template('index.html', result_available=False)

# Running our app -------------------

app.run()