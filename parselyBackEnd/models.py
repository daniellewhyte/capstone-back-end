from django.db import models
from parselyBackEnd.helper import parse_text

# Create your models here.

class Recipe(models.Model):
    url = models.TextField(null=False)
    title = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title

    # @property
    # def recipe(self):
    #     return parse_text(self.url)

    # @property
    # def title(self):
    #     return self.recipe["title"]

    # @property
    # def ingredients(self):
    #     return self.recipe["ingredients"]

    # @property
    # def instructions(self):
    #     return self.recipe["instructions"]

    def save(self, *args, **kwargs):
        recipe_data = parse_text(self.url)
        self.title = recipe_data["title"]
        self.ingredients = recipe_data["ingredients"]
        self.instructions = recipe_data["instructions"]
        super(Recipe, self).save(*args, **kwargs)