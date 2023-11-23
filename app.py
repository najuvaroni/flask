from flask import Flask, render_template, request, redirect


app = Flask(__name__)
class cadInfluencers:
    def __init__(self,nome,plataforma,seguidores,areas):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.areas = areas

lista=[]

@app.route('/Influenciadores')
def pokemon():
    return render_template(' Influenciadores.html',Titulo = "Cadastro de Influenciadores Digitais:",ListaInfluenciadores = lista)

@app.route('/Cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = "Cadastro de  Influenciadores")

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    plataforma = request.form['plataforma']
    seguidores = request.form['seguidores']
    areas = request.form['areas']
    obj =cadInfluencers(nome,plataforma,seguidores,areas)
    lista.append(obj)
    return redirect('/Influenciadores')

if __name__ == '__main__':
    app.run()
