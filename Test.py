from flask import Flask, render_template, request,redirect,url_for
from flask_mysqldb import MySQL
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)
FlaskJSON(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)


@app.route('/')
def Hello():
	return render_template("login.html")

@app.route('/test2', methods=['POST'])
def test2():
	data = request.get_json(force=True)
	username = data['username']
	pwd = data['password']
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO logininfo(Username,Password) VALUES (%s, %s)", (username,pwd))
	mysql.connection.commit()
	cur.close()
	return redirect(url_for('Hello'))


