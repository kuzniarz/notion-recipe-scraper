import json
import recipe_transformer
from recipe_scrapers import scrape_me

TEST_FILE = "../test/data/test_turmeric_cod_curry_with_crispy_coconut_quinoa.json"
TEST_URL = "https://www.mob.co.uk/recipes/turmeric-cod-curry-with-crispy-coconut-quinoa"

def get_json_from(testfile):
    f = open(testfile, "r")
    return json.load(f.read())

def test_build_recipe():
    test_file = get_json_from(TEST_FILE)
    scraper = scrape_me(TEST_URL)
    recipe = recipe_transformer.buildRecipe(TEST_URL, scraper)
    assert test_file == recipe

def test():
    test_build_recipe()

if __name__ == "__main__":
    test()