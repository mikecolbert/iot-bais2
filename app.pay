from flask import Flask
from flask import request
import pymysql
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "Temperature API"
  

@app.route('/temperatures'
def temperatures():
    return "List of temperatures"
   
    
@app.route('/temperature-data/sensors')
def sensors():
    return "Sensors"


if __name__ == '__main__':
    app.run(debug=True)
