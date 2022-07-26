from rest_framework_json_api import serializers
from parselyBackEnd.models import Recipe

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ("title", "ingredients", "instructions")
