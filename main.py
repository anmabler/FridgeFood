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
# def db():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT * FROM recipe''')
#     rows = cur.fetchall()
#     recipes = []
#     for row in rows:
#         recipes.append(row['name'])
#     return str(recipes)

# https://api.spoonacular.com/recipes/716429/information?apiKey=YOUR-API-KEY&includeNutrition=true. 
# https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2
# get('https://api.spoonacular.com/recipes/findByIngredients?information&apiKey=' + API_KEY + '&ingredients=apples,+flour,+sugar&number=2')
@app.route('/api/recipes/findByIngredients/<string:ing>')
def findByIngredients(ing):
    # res = requests.get('https://api.spoonacular.com/recipes/findByIngredients?information&apiKey=' + API_KEY + '&ingredients=apples,+flour,+sugar&number=2')
    res = requests.get('https://api.spoonacular.com/recipes/findByIngredients?information&apiKey=' + API_KEY + '&ingredients=' + ing + '&number=2')
    data = json.loads(res.content)
    return jsonify(data)

@app.route('/api/recipes/findById/<int:id>')
def findById(id):
    # https://api.spoonacular.com/recipes/{id}/information
    # https://api.spoonacular.com/recipes/716429/information?includeNutrition=false
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
        START TRANSACTION;

        INSERT INTO groceries(name)
        VALUES (%s) 
        ON DUPLICATE KEY UPDATE name = name;

        INSERT INTO userxgroceries(userid, groceryid) 
        VALUES (%s, (SELECT idgroceries FROM groceries WHERE groceries.name = %s));

        COMMIT;
        ''',(obj["name"], str(id), obj["name"]))
        # '''
        # INSERT INTO groceries(name)
        # VALUES (%s) 
        # ON DUPLICATE KEY UPDATE name = name;
        # ''',(obj["name"],))
    mysql.connection.commit()
    return (obj)

if __name__ == '__main__':
    app.run(debug=True)