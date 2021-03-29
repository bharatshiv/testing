from flask import *


ob=Flask(__name__)


@ob.route('/')
@ob.route('/index')
def home():
    return("Hello world")


ob.run(debug=True)
