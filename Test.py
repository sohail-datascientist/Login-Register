from flask import Flask, render_template, request,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)


@app.route('/')
def Hello():
	return render_template("login.html")

@app.route('/Test_Phase', methods=['GET', 'POST'])
def Test_Phase():
	if request.method == "POST":
		username = request.form['unam']
		pwd = request.form['pass']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO logininfo(Username,Password) VALUES (%s, %s)", (unam,pas))
		mysql.connection.commit()
		cur.close()
		return redirect(url_for('Hello'))
	
