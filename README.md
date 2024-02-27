# Notion Recipe Scraper
This is the repository for the Notion recipe scraper automation. 

## Background
Initially, this was intended to just host the python script that facilitates the connection between the recipe-scraper API and notion. This script was then accessed via SSH. As this approach was just a barebone prototype which introduced several sercurity aspects, this application will be transformed to be a web service. Therefore, please keep in mind that this documentation may be outdated due to the transformation process.

The application is based on a Python Flask backend with a React frontend.

## Getting Started
### Initialize environment
To work with this project checkout the project sources and initialize the environment:

    python -m venv c:\path\to\myenv

Alternatively you can navigate into the project folder and initialze the environment with:

    python -m venv .

Afterwards you need to activate the given environment by either executing the activation script in the Scripts folder or source the activate file if you are working on a Unix system.

### Download required libraries
This project is based on the [Notion API](https://github.com/ramnes/notion-sdk-py) and the [recipe-scraper](https://github.com/hhursev/recipe-scrapers) project. 

    pip install python-dotenv recipe-scrapers notion-client

In case you're using a proxy with your development system, it may be required to add flags to the installation command

    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org python-dotenv recipe-scrapers notion-client

### Configure environment variables
To use this project, you will need to create a .env file with 2 environment variables. The NOTION_TOKEN can be found in the [integration configuration](https://www.notion.so/my-integrations). If you haven't created an integration yet, simply press "Create new integration". 

The database ID can be taken from the direct link to the database (32 digits after https://www.notion.so/).

    NOTION_TOKEN=<Integration-token-given-by-notion-integration>
    NOTION_DATABASE_ID=<Database-ID>

### Configure Notion database to allow integration interaction
To enable interactions with the created integration, you need to connnect it to the database that should contain the scraped recipies. To do that, navigate to the database in Notion and open the configuration menu by using the three dots in the top right corner. At the bottom of this menu, you can find your configured connections. To connect the database to your integration, press "Add connections" and select your integration.

    ... > Add connections > <your-integration-name>

## TODO
- Automation of environment setup
- Implementation of plugin scripts
