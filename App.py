from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'register'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def Register():
    if request.method == "POST":
        details = request.form

        unam = details['Username']
        pas = details['pass']
        emaill = details['Email']
        cntc = details['Contact']
        ad = details['Address']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO registerinfo(Username,Password,Email,Contact, Address) VALUES (%s, %s,%s, %s, %s)", (unam,pas,emaill,cntc, ad))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('register.html')