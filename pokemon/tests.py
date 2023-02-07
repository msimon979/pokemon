import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


@pytest.mark.django_db
class PokemonCollectionTests(APITestCase):
    """
    Migrations seed the database so the tests are referring to
    objects that already exist on https://msimon979.github.io/pokemon.json
    """

    def test_get_collections(self):
        """
        Test paginated results are returned with a 200
        """
        url = reverse("pokemon_names")

        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()["results"]) == 10

    def test_get_collections_second_page(self):
        """
        Test second page paginated results are returned with a 200
        """
        url = reverse("pokemon_names") + "?page=2"

        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()["results"]) == 10

    def test_get_collections_with_filters(self):
        """
        Test second page paginated results are returned with a 200
        """
        url = reverse("pokemon_names") + "?type_1=grass&type_2=poison"

        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert len(data["results"]) == 10

        for d in data["results"]:
            assert d["type_1"] == "grass"
            assert d["type_2"] == "poison"

    def test_post_new_pokemon(self):
        """
        Test creating a new pokemon is successful
        """
        url = reverse("pokemon_names")

        data = {
            "name": "Bulbasaur_test",
            "type_1": "Grass",
            "type_2": "Poison",
            "total_stats": 318,
            "hp": 45,
            "attack": 49,
            "defense": 49,
            "special_atk": 65,
            "special_def": 65,
            "speed": 45,
            "generation": 1,
            "legendary": False,
        }

        response = self.client.post(url, data=data, format="json")
        assert response.status_code == status.HTTP_201_CREATED

        data = response.json()
        assert data["name"] == "bulbasaur_test"

    def test_post_new_pokemon_fails_due_to_already_existing(self):
        """
        Test creating a new pokemon fails due to name already existing
        """
        url = reverse("pokemon_names")

        data = {
            "name": "Bulbasaur",
            "type_1": "Grass",
            "type_2": "Poison",
            "total_stats": 318,
            "hp": 45,
            "attack": 49,
            "defense": 49,
            "special_atk": 65,
            "special_def": 65,
            "speed": 45,
            "generation": 1,
            "legendary": False,
        }

        response = self.client.post(url, data=data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        data = response.json()
        assert "Bulbasaur already exists" in data

    def test_get_pokemon_by_id(self):
        """
        Test GET pokemon by id returns 200
        """
        url = reverse("pokemon", kwargs={"id": 1})

        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

        data = response.json()

        assert data["name"] == "bulbasaur"

    def test_get_pokemon_by_id_that_does_not_exist_fails(self):
        """
        Test GET pokemon by id that does not exist returns 404
        """
        url = reverse("pokemon", kwargs={"id": 10000})

        response = self.client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
