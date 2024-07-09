from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import MySQLdb.cursors

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/mision')
def mision():
    return render_template('mision.html')

@app.route('/valores')
def valores():
    return render_template('valores.html')

@app.route('/taller')
def talleres():
    return render_template('taller.html')

@app.route('/norma')
def norma():
    return render_template('norma.html')

if __name__ == '__main__':
    app.run(debug=True)
