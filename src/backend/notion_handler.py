import os
from recipe import Recipe
from notion_page_builder import NotionPageBuilder
from notion_client import Client
from dotenv import load_dotenv

class NotionHandler:

    notion_client:Client
    notion_page_builder:NotionPageBuilder

    def __init__(self) -> None:
        # take environment variables from .env.
        load_dotenv()  
        # init Notion API client and NotionPageBuilder
        self.notion_client = Client(auth=os.environ['NOTION_TOKEN'])
        self.notion_page_builder = NotionPageBuilder()

    def post_recipe(self, recipe:Recipe):
        notion_recipe_page = self.notion_page_builder.create_recipe_page(recipe)
        notion_recipe_page["parent"] = {
            "type": "database_id",
            "database_id": os.environ['NOTION_DATABASE_ID']
        }
        self.notion_client.pages.create(**notion_recipe_page)
    
    def retrieve_database(self):
        print(self.notion_client.databases.retrieve(os.environ['NOTION_DATABASE_ID']))
