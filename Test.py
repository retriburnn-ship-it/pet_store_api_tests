import requests
import json

# Create pet

url = "https://petstore.swagger.io/v2/pet"

payload = json.dumps({
  "name": "Pet_Isaiah",
  "photoUrls": [
    "string",
    "string"
  ],
  "id": 1794995510912,
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
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


# Check new pet

url = "https://petstore.swagger.io/v2/pet/:petId"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Update pet

url = "https://petstore.swagger.io/v2/pet"

payload = json.dumps({
  "name": "Pet_Isaiah",
  "photoUrls": [
    "string",
    "string"
  ],
  "id": 1794995510912,
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
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

# Check updated pet

url = "https://petstore.swagger.io/v2/pet/:petId"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Delete pet

url = "https://petstore.swagger.io/v2/pet/:petId"

payload = {}
headers = {
  'api_key': 'string'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

# Check that pet has been deleted

url = "https://petstore.swagger.io/v2/pet/:petId"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
