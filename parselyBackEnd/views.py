from parselyBackEnd.models import Recipe
from parselyBackEnd.serializers import RecipeSerializer, TitleSerializer
from rest_framework import viewsets

# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class TitleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = TitleSerializer