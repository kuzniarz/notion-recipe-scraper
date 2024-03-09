from utils import Utils

class Recipe:
    _title: str
    _duration: int
    _yields: str
    _tags: list[str]
    _external: str
    _ingredients: list[str]
    _instructions: list[str]
    _image: str

    def __init__(self, title:str, duration:int=0, yields=1, tags=[], ingredients=[], instructions=[], external='', image='') -> None:
        assert isinstance(title, str), "title must be a string"
        assert isinstance(duration, int), "duration must be an int"
        assert isinstance(duration, int), "duration must be an int"
        assert isinstance(yields, int), "yield must be an int"
        assert isinstance(external, str), "external must be a str"
        assert isinstance(image, str), "image url must be a str"
        assert Utils.is_list_of_strings(tags), "tags must be a list of str"
        assert Utils.is_list_of_strings(ingredients), "ingredients must be a list of str"
        assert Utils.is_list_of_strings(instructions), "instructions must be a list of str"

        self._title = title
        self._duration = duration
        self._yields = yields
        self._external = external
        self._tags = tags
        self._ingredients = ingredients
        self._instructions = instructions
        self._image = image

    def __str__(self) -> str:
        return  str({"title":       self._title,
                "duration":     self._duration,
                "yields":       self._yields,
                "external":     self._external,
                "tags":         self._tags,
                "ingredients":  self._ingredients,
                "instructions": self._instructions,
                "image": self._image})

    def __eq__(self, __value: object) -> bool:
        return (self._title == __value.title) and \
        (self._duration == __value.duration) and \
        (self._yields == __value.yields) and \
        (self._external == __value.external) and \
        (self._tags == __value.tags) and \
        (self._ingredients == __value.ingredients) and \
        (self._instructions == __value.instructions) and \
        (self._image == __value.image)
    
    def set_title(self, title:str):
        assert isinstance(title, str), "title must be an str"
        self._title = title

    def set_duration(self, duration:int):
        assert isinstance(duration, int), "duration must be an int"
        self._duration = duration

    def set_yield(self, yields:int):
        assert isinstance(yields, int), "yield must be an int"
        self._yields = yields

    def set_external(self, external:str):
        assert isinstance(external, str), "external must be an str"
        self._external = external

    def set_tags(self, tags:list):
        assert Utils.is_list_of_strings(tags), "tags must be a list of str"
        self._tags = tags

    def set_ingredients(self, ingredients:list):
        assert Utils.is_list_of_strings(ingredients), "ingredients must be a list of str"
        self._ingredients = ingredients

    def set_instructions(self, instructions:list):
        assert Utils.is_list_of_strings(instructions), "instructions must be a list of str"
        self._instructions = instructions

    def set_image(self, image:str):
        assert isinstance(image, str), "image must be a str"
        self._image = image

    def title(self) -> str:
        return self._title

    def duration(self) -> int:
        return self._duration

    def yields(self) -> int:
        return self._yields

    def external(self) -> str:
        return self._external

    def tags(self) -> list:
        return self._tags

    def ingredients(self) -> list:
        return self._ingredients

    def instructions(self) -> list:
        return self._instructions
    
    def image(self) -> str:
        return self._image
    