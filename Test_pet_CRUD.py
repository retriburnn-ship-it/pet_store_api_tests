import requests
from jsonschema import validate

from Variables import pet_create_data, base_url, pet_schema

def test_status_code_is_200(create_pet_response):
    assert create_pet_response.status_code == 200

def test_response_is_json(create_pet_response):
    assert create_pet_response.json() == pet_create_data

def test_response_is_in_schema(create_pet_response):
    assert create_pet_response.json() == pet_schema

def test_response_is_in_schema(create_pet_response):
    validate(instance=create_pet_response.json(), schema=pet_schema)

def test_same_name(create_pet_response):
    pet = create_pet_response.json()
    assert pet["name"] == pet_create_data["name"]
    print(' Pet name is', pet["name"])
    print(' Pet id is', pet["id"])

def test_pet_exists_in_db(pet_id):
    response = requests.get(f"{base_url}/pet/{pet_id}")
    pet_page = response.json()
    assert response.status_code == 200
    assert response.json() == pet_create_data
    print(' Pet id is', pet_page["id"])

