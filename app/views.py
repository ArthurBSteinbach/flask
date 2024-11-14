from app import app
from flask import render_template, url_for
@app.route('/')
def homepage():
    
    idade = 25
    usuario = 'Arthon Lambda'
    context = {
        'idade':idade,
        'usuario':usuario
    }
    return render_template('index.html', message='estou conectado ao back-end!',context=context)

@app.route('/news/')
def newpage():
    return 'Nova página'