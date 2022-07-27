from rest_framework_json_api import serializers
from parselyBackEnd.models import Recipe

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ("title", "ingredients", "instructions")

    def create(self, recipe_data):
        return Recipe(title=recipe_data["title"], 
                        ingredients=recipe_data["ingredients"], 
                        instructions=recipe_data["instructions"])