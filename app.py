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
    'client_flags': [pymysql.connector.ClientFlag.SSL],
    'ssl_ca': './DigiCertGlobalRootG2.crt.pem'
}

@app.route('/')
def index():
    return "Temperature API"
  

@app.route('/temperatures')
def temperatures():
    return "List of temperatures"
   
# GET request
    try:
        conn = pymysql.connector.connect(**config)
                
    except pymysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cur = conn.cursor()
    #cur = conn.cursor()

    query = "SELECT * FROM temperaturelog ORDER BY readTime DESC"
    cur.execute(query)
    
    results = cur.fetchall()

    print("----------")
    print("Total number of rows in table: ", cur.rowcount)
    print("----------")
    print(results)
        
    cur.close()

    conn.close()
            
    return (results)


@app.route('/sensors')
def sensors():
    return "List of sensors"


if __name__ == '__main__':
    app.run(debug=True)
