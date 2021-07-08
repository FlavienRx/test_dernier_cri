import requests
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from api.models import Move, Pokemon, Type


class Command(BaseCommand):
    help = "Fill database with PokeAPI's data"

    def handle(self, *args, **options):
        base_url = "https://pokeapi.co/api/v2/"

        # Get twenty first pokemons
        db_count = Pokemon.objects.count()

        # If the database is not up to date
        if db_count < 20:
            for i in range(1, 21):
                response = requests.get(base_url + "pokemon/" + str(i))
                data = response.json()

                try:
                    # Create the pokemon
                    pokemon = Pokemon.objects.create(
                        poke_api_id=data["id"],
                        name=data["name"],
                        height=data["height"],
                        weight=data["weight"],
                        small_image_url=data["sprites"]["front_default"],
                        large_image_url=data["sprites"]["other"]["official-artwork"][
                            "front_default"
                        ],
                    )

                    # Add pokemon's types
                    for data_type in data["types"]:
                        (type, created) = Type.objects.get_or_create(
                            # Get type id from url
                            # to improve performance and reduce API calls
                            poke_api_id=int(data_type["type"]["url"].split("/")[-2]),
                            name=data_type["type"]["name"],
                        )
                        pokemon.types.add(type)

                    # Add pokemon's moves
                    for data_move in data["moves"]:
                        (move, created) = Move.objects.get_or_create(
                            # Get move id from url
                            # to improve performance and reduce API calls
                            poke_api_id=int(data_move["move"]["url"].split("/")[-2]),
                            name=data_move["move"]["name"],
                        )
                        pokemon.moves.add(move)

                    pokemon.save()

                except IntegrityError:
                    # Do noting
                    pass
