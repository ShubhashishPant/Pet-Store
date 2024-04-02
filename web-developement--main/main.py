from flask import Flask, render_template, request
 
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'new_db'

mysql = MySQL(app)
@app.route('/')
def index():
    return render_template ('Welcome page.html')
@app.route('/product')
def product():
    return render_template("product.html")
@app.route('/american')
def pitbull():
    return render_template("american.html")
@app.route('/cart')
def cart():
    return render_template("cart.html")
@app.route('/account')
def account():
    return render_template("account.html")
@app.route('/pug')
def pug():
    return render_template("pug.html")
@app.route('/Welcome Page')
def welcome():
    return render_template("Welcome_Page.html")
@app.route('/tibetian')
def tibetian():
    return render_template("tibetian mastiff.html")
# @app.route('/tibetian')
# def tibetian():
#     return render_template("tibetian mastiff.html")
@app.route('/login_validation', methods = ['POST'])
def login_validation():
    email = request.form.get('username')
    password = request.form.get('password')
    cur = mysql.connection.cursor()
    
    cur.execute("""SELECT * FROM `mytable` WHERE `email` LIKE %s AND `password` LIKE %s""", (email, password))

    mytable = cur.fetchall()
    if len(mytable) > 0:
        return render_template ('Welcome page.html')
    else: 
        return render_template("account.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('uname')
        email = request.form.get('uemail')
        password = request.form.get('upassword')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mytable (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        mysql.connection.commit()
        cur.close()
        return "Registered successfully"
    
@app.route('/account/update', methods=['POST'])
def update_user():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    cur = mysql.connection.cursor()
    cur.execute("UPDATE mytable SET name=%s, email=%s WHERE password=%s", (name, email, password))
    mysql.connection.commit()
    cur.close()
    return render_template("welcome page.html")

if __name__ == "__main__":
    app.run(debug= True)