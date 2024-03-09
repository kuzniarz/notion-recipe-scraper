from flask import Flask, current_app
from flask import request
from recipe_factory import RecipeFactory
from notion_handler import NotionHandler

app:Flask = Flask(__name__)
notion_handler = NotionHandler()
recipe_factory  = RecipeFactory()

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/scrape-me/url=<url>')
def scrape_recipe(url):
    recipe = recipe_factory.scrape_recipe(url.replace('_', '/'))
    notion_handler.post_recipe(recipe)
    return str(recipe)

if __name__ == '__main__':
    app.run(debug=True)