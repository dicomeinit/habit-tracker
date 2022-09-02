import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "hihd87w9hq9cs0d0cjw093v0d9s93j",
    "username": "dianaber",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
