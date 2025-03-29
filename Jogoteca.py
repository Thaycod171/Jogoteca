from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['mario' , 'chash' , 'valorant']
    return render_template('lista.html' , titulo='Jogos' , Jogos=lista)

app.run()