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

dbconfig = {
    'host' : dbhost, 
    'user' : dbuser, 
    'password' : dbpass, 
    'db' : dbname, 
    #'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': './DigiCertGlobalRootG2.crt.pem',
    'cursorclass' : pymysql.cursors.DictCursor
}

@app.route('/')
def index():
    return "Temperature API"
  

@app.route('/temperatures')
def temperatures():
    
    # GET request
    conn = pymysql.connect(**dbconfig)

    cur = conn.cursor()

    query = "SELECT * FROM temperaturelog ORDER BY readTime DESC"
    cur.execute(query)
    
    results = cur.fetchall()

    print("----------")
    print("Total number of rows in table: ", cur.rowcount)
    print("----------")
    print(results)
        
    cur.close()

    conn.close()
            
    return results


@app.route('/sensors')
def sensors():
    return "List of sensors"


if __name__ == '__main__':
    app.run(debug=True)
