from django.shortcuts import render
from parselyBackEnd.models import Recipe
from parselyBackEnd.serializers import RecipeSerializer
from rest_framework import viewsets

# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer