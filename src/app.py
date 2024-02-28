from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/scrape-me/url=<url>')
def scrape_recipe(url):
    return f"This seemed to work, boa! The url {url} is going to be processed!"

if __name__ == '__main__':
    app.run(debug=True)