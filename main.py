from flask import *
from flaskext.mysql import MySQL

app=Flask(__name__)
app.secret_key='hello123'

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='mydata'

mysql=MySQL()
mysql.init_app(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dologin',methods=['POST'])
def dologin():
    username=request.form['username']
    password=request.form['password']
    mycon=mysql.connect()
    mycur=mycon.cursor()
    info=[username,password]
    mycur.execute("select * from user where username=%s and password=%s",info)
    data=mycur.fetchone()
    if(data):
        session['user']=data[1]
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')
app.run(debug=True)
