from recipe import Recipe
from recipe_scrapers import scrape_me

class RecipeFactory:

    def __init__(self) -> None:
        pass

    def create_recipe(title, duration, yields, tags, ingredients, instructions):
        return Recipe(title, duration, yields, tags, ingredients, instructions)
    
    def scrape_recipe(self, url:str) -> Recipe:
        scraper = scrape_me(url)
        return Recipe(title=scraper.title(),
           duration=scraper.total_time(), 
           yields=int(scraper.yields().replace(' servings', '')), 
           external=url,
           tags=[],
           ingredients=scraper.ingredients(),
           instructions=scraper.instructions_list(),
           image=scraper.image())

    