from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

with open('db.yaml', 'r') as file:
    db = yaml.safe_load(file)

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM names")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', names = data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        score = request.form['score']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO names (name, id, score) VALUES (%s, %s, %s)', (name, id, score))
        mysql.connection.commit()
        return redirect(url_for('Index'))
    
@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_delete):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM names WHERE id = %s", (id_delete,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/update',methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        score = request.form['score']

        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE names
               SET name = %s, score = %s
               WHERE id = %s
            """, (name, score, id))
        mysql.connection.commit()
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug = True)