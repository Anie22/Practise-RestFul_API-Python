import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    "title": "Done"
}

get_response = requests.post(endpoint)