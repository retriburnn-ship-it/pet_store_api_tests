import random
from faker import Faker

fake = Faker()

base_url = 'https://petstore.swagger.io/v2'

pet_schema = {"type":"object",
              "required":["id","name","photoUrls"],
              "properties":
                  {
                      "id":{"type":"integer"},
                      "name":{"type":"string"},
                      "photoUrls":{"type":"array","items":{"type":"string"}},
                      "category":{"type":"object","properties":{"id":{"type":"integer"},"name":{"type":"string"}}},
                      "tags":{"type":"array","items":{"type":"object","properties":{"id":{"type":"integer"},"name":{"type":"string"}}}},
                      "status":{"type":"string","enum":["available","pending","sold"]}}}

pet_create_data = {
      "name": f"Pet_{fake.first_name()}",
      "photoUrls": [
        "string",
        "string"
      ],
      "id": random.randint(1000, 9999),
      "category": {
        "id": 1101,
        "name": "string"
      },
      "tags": [
        {
          "id": 8937,
          "name": "string"
        },
        {
          "id": 1485,
          "name": "string"
        }
      ],
      "status": "available"
    }
pet_create_headers = {
      'Content-Type': 'application/json'
    }