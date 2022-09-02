import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "dianaber"
TOKEN = "hihd87w9hq9cs0d0cjw093v0d9s93j"
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": "20220903",
    "quantity": "2.30",

}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)