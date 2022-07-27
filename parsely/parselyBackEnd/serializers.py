from rest_framework_json_api import serializers
from parselyBackEnd.models import Recipe

class RecipeSerializer(serializers.HyperlinkedModelSerializer):

    title = serializers.ReadOnlyField()
    ingredients = serializers.ReadOnlyField()
    instructions = serializers.ReadOnlyField()

    class Meta:
        model = Recipe
        fields = ["url", "title", "ingredients", "instructions"]
