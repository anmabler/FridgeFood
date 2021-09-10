from flask import Flask
from flask import request, jsonify

from flask_mysqldb import MySQL
from instance.config import API_KEY
from pip._vendor import requests
import json


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py') # Get configuration for MySQL db

mysql = MySQL(app)

@app.route('/')
def greeting():
    return "Hello from python"

@app.route('/api/recipes/findByIngredients/<string:ing>')
def findByIngredients(ing):
    res = requests.get('https://api.spoonacular.com/recipes/findByIngredients?information&apiKey=' + API_KEY + '&ingredients=' + ing + '&number=2')
    data = json.loads(res.content)
    return jsonify(data)

@app.route('/api/recipes/findById/<int:id>')
def findById(id):
    res = requests.get('https://api.spoonacular.com/recipes/' + str(id) + '/information?apiKey=' + API_KEY + '&includeNutrition=false')
    data = json.loads(res.content)
    return jsonify(data)

@app.route('/api/users/<int:id>')
def getUserByid(id):
    cur = mysql.connection.cursor()
    cur.execute(#'SELECT * FROM user WHERE iduser = %s'
                '''
                SELECT g.name AS groceryname
                FROM user as u, userxgroceries as uxg, groceries as g
                WHERE uxg.groceryid = g.idgroceries 
                AND (u.iduser = uxg.userid) 
                AND u. iduser = %s
                ''', (str(id)))
    rows = cur.fetchall()
    info = []
    for row in rows:
        info.append(row)
    return (rows)

@app.route('/api/users/<int:id>', methods=["POST"])
def addGroceriesToDb(id):
    obj = request.get_json()

    print(obj["name"])
    cur = mysql.connection.cursor()
    cur.execute(
        '''
        INSERT INTO groceries(name)
        VALUES (%s) 
        ON DUPLICATE KEY UPDATE name = name;
        ''',(obj["name"],))
    mysql.connection.commit()
    cur.execute('''
        INSERT INTO userxgroceries(userid, groceryid) 
        VALUES (%s, (SELECT idgroceries FROM groceries WHERE groceries.name = %s));
        ''',(str(id), obj["name"],))
    mysql.connection.commit()
    return (obj)

if __name__ == '__main__':
    app.run(debug=True)