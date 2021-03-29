from flask import *


app=Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return("Hello world")


app.run(debug=True)
