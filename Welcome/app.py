from flask import Flask


# --- --- --- --- --- ---  Definimos nosso app flask --- --- --- --- --- --- 

app = Flask(__name__)

# Flask(__name__) will print ("<Flask 'app'>"), sendo que 'app' não se refere ao nome da variável, mas aquele do arquivo que está rodando.
# print(app) --> <Flask 'app'>"
# print(__name__) --> __main__
# print(Flask(__name__)) --> <Flask 'app'>"

# --- --- --- --- --- --- Especificamos o que ocorre em nosso app --- --- --- --- --- --- 

@app.route('/') # app.route define a rota em que aquele método está rodando, seria como o urlpatterns do Django
def welcome():
    return home() # Retornando outra função (funções de página) é possivel redirecionar o usuário

@app.route('/home')
def home():
    return 'This is my first flask app! <3 You were redirect from the url /'


# --- --- --- --- --- --- Rodamos nosso app flask --- --- --- --- --- --- 

app.run() # Roda o aplicativo flash