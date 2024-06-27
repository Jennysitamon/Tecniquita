from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
