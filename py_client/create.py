import requests

headers = {'Authorization': 'Bearer af872ee22519a9b46fc3e57d061c06f27bb7aa54'}


endpoint = "http://localhost:8000/api/products/"

data = {
    'title':'This field is done',
    'price': 32.99,
}


get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
