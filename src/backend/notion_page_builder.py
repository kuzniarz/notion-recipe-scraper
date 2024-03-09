import os
from recipe import Recipe

class NotionPageBuilder:
    page = {}

    def __init__(self) -> None:
        pass

    def item_list(self, itemlist):
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

    def h2_header(self, text):
        return {
            "object": "block",
                "heading_2": {
                    "rich_text": [{"text": {"content": text }}]
                }
            }

    def image(self, img):
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
    
    def build_page_content(self, ingredients, instructions_list, recipe_image):
        ingredients_content = [self.h2_header("Ingredients")]
        ingredients_content.extend(self.item_list(ingredients))

        instructions_content = [self.h2_header("Instructions")]
        instructions_content.extend(self.item_list(instructions_list))
        instructions_content.extend(self.image(recipe_image))
        
        return ingredients_content, instructions_content

    def column(self, content):
        return {
            "object": "block",
            "type": "column",
            "column": {
                "children": content
            }
        }

    def page_columns(self, ingredients, instructions, recipe_image):
        ingredients_content, instructions_content = self.build_page_content(ingredients, instructions, recipe_image)
        return [
            self.column(ingredients_content),
            self.column(instructions_content)
            ]

    def column_list(self, content):
        return [{
            "object": "block",
            "type": "column_list",
            "column_list": {
                "children": content
            }
        }]

    def create_recipe_page(self, recipe:Recipe):    
        self.page["cover"] = {
            "type": "external",
            "external": {"url": recipe.image()}
            }
        self.page["icon"] = {
            "type": "external",
            "external": {"url": "https://www.notion.so/icons/dining_gray.svg"}
        }
        self.page["parent"] = {
            "type": "database_id",
            "database_id": os.environ['NOTION_DATABASE_ID']
        }
        self.page["properties"] = {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": recipe.title()
                            }
                        }
                    ]
                },
                "Prep Time": {
                    "number" : recipe.duration()
                },
                "Serves": {
                    "number" : recipe.yields()
                },
                "URL": {
                    "url": recipe.external()
                }
        }
        self.page["children"] = self.column_list(
            self.page_columns(
                recipe.ingredients(), recipe.instructions(), recipe.image()
                )
            )
        return self.page