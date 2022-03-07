from flask import Flask, request, render_template, redirect

app = Flask(__name__)


def index():
    """."""
    pass


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    """
    Sign up route method.

    Returns a page for GET and process new user for POST request.
    """
    if request.method == "POST":
        cpf = request.form.get('cpf')
        name = request.form.get('name')
        cep = request.form.get('cep')
        return redirect("/")

    return render_template("sign_up.html")


app.run()
