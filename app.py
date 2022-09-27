from flask import Flask
from flask import request
import pymysql
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return "Temperature API"
  

@app.route('/temperatures')
def temperatures():
    return "List of temperatures"
   
    
@app.route('/sensors')
def sensors():
    return "List of sensors"


if __name__ == '__main__':
    app.run(debug=True)
