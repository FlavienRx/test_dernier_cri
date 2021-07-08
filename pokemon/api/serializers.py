from rest_framework import serializers

from .models import Move, Pokemon, Type


class TypeSerializer(serializers.ModelSerializer):
    """
    Type Model Serializer
    """

    class Meta:
        model = Type
        fields = [
            "poke_api_id",
            "name",
        ]


class MoveSerializer(serializers.ModelSerializer):
    """
    Move Model Serializer
    """

    class Meta:
        model = Move
        fields = [
            "poke_api_id",
            "name",
        ]


class PokemonListSerializer(serializers.ModelSerializer):
    """
    Pokemon Model List Serializer
    """

    class Meta:
        model = Pokemon
        fields = [
            "poke_api_id",
            "name",
            "small_image_url",
        ]


class PokemonDetailSerializer(serializers.ModelSerializer):
    """
    Pokemon Model Detail Serializer
    """

    types = TypeSerializer(many=True, read_only=True)
    moves = MoveSerializer(many=True, read_only=True)

    class Meta:
        model = Pokemon
        fields = [
            "poke_api_id",
            "name",
            "height",
            "height",
            "weight",
            "types",
            "moves",
            "large_image_url",
        ]
