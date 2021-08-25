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
@app.route('/api/recipes/findByIngredients')
def findByIngredients():
    res = requests.get('https://api.spoonacular.com/recipes/findByIngredients?information&apiKey=' + API_KEY + '&ingredients=apples,+flour,+sugar&number=2')
    data = json.loads(res.content)
    return jsonify(data)

@app.route('/api/recipes/findById/<int:id>')
def findById(id):
    # https://api.spoonacular.com/recipes/{id}/information
    # https://api.spoonacular.com/recipes/716429/information?includeNutrition=false
    res = requests.get('https://api.spoonacular.com/recipes/' + str(id) + '/information?apiKey=' + API_KEY + '&includeNutrition=false')
    data = json.loads(res.content)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)