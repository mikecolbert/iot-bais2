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
    'ssl_ca': './DigiCertGlobalRootG2.crt.pem',
    'cursorclass' : pymysql.cursors.DictCursor
}

@app.route('/')
def index():
    return "Temperature API"
  

@app.route('/temperatures', methods=['GET', 'POST'])
def temperatures():
#POST request
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            #return json

            sensorId = request.json['sensorNum']
            temperature = request.json['temperature']
            humidity = request.json['humidity']
 
            conn = pymysql.connect(**dbconfig)
            cur = conn.cursor()

            query = "INSERT INTO `temperaturelog` (`readTime`, `sensorId`, `temperature`, `humidity`) VALUES (CURRENT_TIMESTAMP(), %s, %s, %s);"
            cur.execute(query, (sensorId, temperature, humidity)) # values need to be specified as one tuple - in parens
            conn.commit() # the connection is not autocommited by default - commit to save changes

            print(f"{cur.rowcount} record inserted into temperaturelog table")

            cur.close()
            conn.close()
            
            print(sensorId)
            print(temperature)
            print(humidity)

            return f"{json} inserted into temperatureLog table"
            
        else:
            return 'Content-Type not supported!'

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
