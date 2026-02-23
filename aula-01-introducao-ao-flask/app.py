# Comentário em Python
# Importando o Flask na aplicação
from flask import Flask, render_template #render_template renderiza as páginas HTML

# Carregando o Flask em uma variável
app = Flask(__name__, template_folder='views')
#__name__ é uma variável de ambiente do Pyton que tem o nome do Módulo atual.

# CRANDO A ROTA PRINCIPAL DO SITE
@app.route('/')
#def serve para crar funções no Python
def home():
    return render_template('index.html')

@app.route('/games')

def games():
    return render_template('games.html')

@app.route('/console')

def console():
    return render_template('consoles.html')

# Iniciand o servidor web
if __name__ == '__main__':
    app.run()
    # Verificando se app.py for o arquivo principal ele inicia o servidor