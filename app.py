from flask import Flask
from flask import request
import pymysql
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

dbuser = os.environ.get('DBUSER')
dbpass = os.environ.get('DBPASS')
dbhost = os.environ.get('DBHOST')
dbname = os.environ.get('DBNAME')


@app.route('/')
def index():
    return "Temperature API"
  

@app.route('/temperatures')
def temperatures():
    return f"List of temperatures - {dbhost}"
   
    
@app.route('/sensors')
def sensors():
    return f"List of sensors - {dbname}"


if __name__ == '__main__':
    app.run(debug=True)
