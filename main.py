from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

mysql = MySQL(app)

@app.route('/')
def recipes():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM recipe''')
    rows = cur.fetchall()
    recipes = []
    for row in rows:
        recipes.append(row['name'])
    return str(recipes)

if __name__ == '__main__':
    app.run(debug=True)