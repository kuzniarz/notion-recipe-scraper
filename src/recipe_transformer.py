import os
import sys
from notion_client import Client
from recipe_scrapers import scrape_me
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()  # take environment variables from .env.
notion = Client(auth=os.environ['NOTION_TOKEN'])

def print_user_list():
    list_users_response = notion.users.list()
    pprint(list_users_response)

def loadRecipeFromURL(url):
    scraper = scrape_me(url)
    return url, scraper

def saveRecipeToNotion(url, scraper):
    #pprint(notion.databases.retrieve(os.environ['NOTION_DATABASE_ID']))
    # pprint(notion.pages.retrieve("ADD YOUR PAGE ID HERE")) 
    notion.pages.create(**{
        "cover": {
            "type": "external",
            "external": {
                "url": scraper.image()
            }
        },
        'icon': {
            "type": "external",
            "external": {
                "url": "https://www.notion.so/icons/dining_gray.svg"}
        },
        "parent": {
            "type": "database_id",
            "database_id": os.environ['NOTION_DATABASE_ID']
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": scraper.title()
                        }
                    }
                ]
            },
            "Prep Time": {
                "number" : scraper.total_time()
            },
            "Serves": {
                "number" : int(scraper.yields().replace(' servings', ''))
            },
            "URL": {
                "url": url
            }
        }
    })

#General Idea of this script
#Take Argument and save it to variable
#Use library to get recipe data
#Use Notion API to create recipe entry
#If successful:
#   return 1;
#else:
#   return 0;

def main():
    try:
        #print_user_list(); 
        url, scraper = loadRecipeFromURL(sys.argv[1])
        saveRecipeToNotion(url, scraper)
        return 1;
    except Exception as e: 
        print("An exception occurred")
        print(e)
        return 0;

if __name__ == "__main__":
    main()
