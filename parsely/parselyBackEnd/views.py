from django.shortcuts import render
from parselyBackEnd.models import Recipe
from parselyBackEnd.serializers import RecipeSerializer
from rest_framework import viewsets
from parselyBackEnd.helper import parse_text
import json

# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # def initialize_request(self, request, *args, **kwargs):
    #     request_data = request.data
    #     recipe_url = request_data["url"]
    #     my_data = json.loads(request)
    #     my_data["body"] = parse_text(recipe_url)
    #     return
    def create(self, request):
        request_data = json.loads(request.body)
        #recipe_url = request_data["url"]
        model_data = parse_text(request_data["data"]["attributes"]["url"])
        return super().create(model_data)

    # def perform_create(self, serializer):
    #     request = serializer.context('request')
    #     request_data = request.data
    #     recipe_url = request_data["url"]
    #     recipe_data = parse_text(recipe_url)
    #     serializer.save(title=recipe_data["data"]["attributes"]["title"], 
    #                     ingredients=recipe_data["data"]["attributes"]["ingredients"],
    #                     instructions=["data"]["attributes"]["instructions"])
