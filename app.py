from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'base_gordo'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/paginas')
def paginas():
    return render_template("paginas.html")

@app.route('/recomendaciones', methods=['GET', 'POST'])
def recomendaciones():
    if request.method == 'POST': 
        nombres = request.form['nombre']
        descripcions = request.form['descripcion']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO base_gordo.datos (nombre,descripcion) values (%s,%s)",(nombres,descripcions))
        mysql.connection.commit()
        cur.close()
    return render_template("recomendaciones.html")

if __name__ == '__main__': 
    app.run(debug=True,)