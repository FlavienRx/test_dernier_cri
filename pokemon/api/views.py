from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Pokemon
from .serializers import PokemonDetailSerializer, PokemonListSerializer


class PokemonViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving pokemons.
    """

    def list(self, request):
        queryset = Pokemon.objects.all()
        serializer = PokemonListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        pokemon = get_object_or_404(Pokemon, poke_api_id=pk)
        serializer = PokemonDetailSerializer(pokemon)
        return Response(serializer.data)
