import os
import sys
import traceback
from notion_client import Client
from recipe_scrapers import scrape_me
from dotenv import load_dotenv
from pprint import pprint

# THIS NEEDS MASSIVE STRUCTURAL REWORK, but version 0.1 is done 

load_dotenv()  # take environment variables from .env.
notion = Client(auth=os.environ['NOTION_TOKEN'])

def loadRecipeFromURL(url):
    scraper = scrape_me(url)
    return url, scraper

def item_list(itemlist):
    json_list = []
    for item in itemlist:
        json_list.append({
            "object": "block",
            "bulleted_list_item": {
                "rich_text": [
                    {
                        "text": {
                            "content": item,
                        }
                    }
                ],
                "color": "default"
            }
        })
    return json_list

def h2_header(text):
    return {
        "object": "block",
            "heading_2": {
                "rich_text": [{"text": {"content": text }}]
            }
        }

def image(img):
    return [{
        "object": "block",
        "type": "image",
        "image": {
            "type": "external",
            "external": {
 	  	        "url": img
            }
        }
    }]

def build_page_content(ingredients, instructions_list, recipe_image):
    ingredients_content = [h2_header("Ingredients")]
    ingredients_content.extend(item_list(ingredients))

    instructions_content = [h2_header("Instructions")]
    instructions_content.extend(item_list(instructions_list))
    instructions_content.extend(image(recipe_image))
    
    return ingredients_content, instructions_content

def column(content):
    return {
        "object": "block",
        "type": "column",
        "column": {
            "children": content
        }
    }

def page_columns(ingredients, instructions, recipe_image):
    ingredients_content, instructions_content = build_page_content(ingredients, instructions, recipe_image)
    return [
          column(ingredients_content),
          column(instructions_content)
        ]

def column_list(content):
    return [{
        "object": "block",
        "type": "column_list",
        "column_list": {
            "children": content
        }
    }]

def buildRecipe(url, recipe_image, title, total_time, servings, ingredients, instructions_list):
    recipe = {}
    recipe["cover"] = {
        "type": "external",
        "external": {"url": recipe_image}
        }
    recipe["icon"] = {
        "type": "external",
        "external": {"url": "https://www.notion.so/icons/dining_gray.svg"}
    }
    recipe["parent"] = {
        "type": "database_id",
        "database_id": os.environ['NOTION_DATABASE_ID']
    }
    recipe["properties"] = {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            },
            "Prep Time": {
                "number" : total_time
            },
            "Serves": {
                "number" : servings
            },
            "URL": {
                "url": url
            }
    }
    recipe["children"] = column_list(page_columns(ingredients, instructions_list, recipe_image))
    return recipe

def saveRecipeToNotion(url, scraper):
    #pprint(notion.databases.retrieve(os.environ['NOTION_DATABASE_ID']))
    recipe = buildRecipe(
        url, scraper.image(), 
        scraper.title(), 
        scraper.total_time(), 
        int(scraper.yields().replace(' servings', '')), 
        scraper.ingredients(),
        scraper.instructions_list()
    )
    recipe["parent"] = {
        "type": "database_id",
        "database_id": os.environ['NOTION_DATABASE_ID']
    }
    notion.pages.create(**recipe)

def main():
    try:
        url, scraper = loadRecipeFromURL(sys.argv[1])
        saveRecipeToNotion(url, scraper)
        return 1;
    except Exception as e: 
        print("An exception occurred")
        print(e)
        traceback.print_exc() 
        return 0;

if __name__ == "__main__":
    main()
