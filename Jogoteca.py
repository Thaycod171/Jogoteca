from flask import Flask, render_template , request


class Jogo:
    def __init__(self , nome , categoria , console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
Jogo1 = Jogo('Valorant' , 'tiro' , 'pc')
Jogo2 = Jogo('Genshin' , 'rpg' , 'pc/mobile')
Jogo3 = Jogo('lol' , 'magia' , 'pc/mobile')

lista = [Jogo1 , Jogo2 , Jogo3]
    
app = Flask(__name__)


@app.route('/inicio')
def ola():

    return render_template('lista.html' , titulo='Jogos' , Jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html' , titulo ='Novo Jogo')


@app.route('/criar')
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome , categoria , console)
    lista.append(jogo)
    return render_template('listahtml' , titulo='Jogo' , Jogos=lista)
app.run()