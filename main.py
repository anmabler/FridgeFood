from flask import Flask
from flask import request, jsonify

from flask_mysqldb import MySQL
from instance.config import API_KEY
from pip._vendor import requests


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

mysql = MySQL(app)

# @app.route('/')
# def recipes():
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

@app.route('/recipes')
def recipes():
    
    res = requests.get('https://api.spoonacular.com/recipes/findByIngredients?information&apiKey=' + API_KEY + '&ingredients=apples,+flour,+sugar&number=2')
    json_data = res.json()
    recipe_list = []

    for data in json_data:
        recipe_list.append(data['title'])
    return str(recipe_list)
    


if __name__ == '__main__':
    app.run(debug=True)