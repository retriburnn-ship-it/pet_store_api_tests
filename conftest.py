import pytest
import requests
from Variables import base_url, pet_create_data


@pytest.fixture(scope="module")
def create_pet_response():
    return requests.post(f"{base_url}/pet", json=pet_create_data)

@pytest.fixture(scope="module")
def pet_id(create_pet_response):
    pet = create_pet_response.json()
    assert "id" in pet, "Id не найден в ответе"
    return pet["id"]

