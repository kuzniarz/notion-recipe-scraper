import os
from notion_client import Client
from recipe_scrapers import scrape_me
from dotenv import load_dotenv
from pprint import pprint

def get_user_list():
    notion = Client(auth=os.environ['NOTION_TOKEN'])
    list_users_response = notion.users.list()
    #pprint(list_users_response)

#General Idea of this script
#Take Argument and save it to variable
#Use library to get recipe data
#Use Notion API to create recipe entry
#If successful:
#   return 1;
#else:
#   return 0;

def main():
    load_dotenv()  # take environment variables from .env.
    try:
        get_user_list();
        return 1;
    except:
        print("An exception occurred")
        return 0;

if __name__ == "__main__":
    main()
