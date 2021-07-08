from django.test import Client, TestCase
from django.urls import reverse

from .models import Move, Pokemon, Type


class PokemonModelTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        type = Type.objects.create(poke_api_id=1, name="grass")
        move = Move.objects.create(poke_api_id=1, name="cut")
        pokemon = Pokemon.objects.create(
            poke_api_id=1,
            name="bulbasaur",
            height=10,
            weight=10,
            small_image_url="",
            large_image_url="",
        )

        pokemon.types.add(type)
        pokemon.moves.add(move)
        pokemon.save()

        self.client = Client()

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_api_list(self):
        response = self.client.get("/api/pokemon/")
        self.assertEqual(response.status_code, 200)

    def test_api_detail(self):
        response = self.client.get("/api/pokemon/1/")
        self.assertEqual(response.status_code, 200)

    def test_api_detail_not_found(self):
        response = self.client.get("/api/pokemon/0/")
        self.assertEqual(response.status_code, 404)
