from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

mysql = MySQL(app)

@app.route('/')
def recipes():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM recipe''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == '__main__':
    app.run(debug=True)