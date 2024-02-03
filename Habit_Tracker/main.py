import requests
import datetime

pixela_endpoints = "https://pixe.la/v1/users"
username = "manish007g"
token = "jfduaij383hhd0swdd"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoints, json=user_params)
# print(response.text)

graph_endpoints = f"{pixela_endpoints}/{username}/graphs"

graph_configs = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token
}
#
# response = requests.post(url=graph_endpoints, json=graph_configs, headers=headers)
# print(response.text)
dt = datetime.datetime

today = dt(year=2024, month=1, day=19)

graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.2"
}

graph_post_endpoint = f"{graph_endpoints}/graph1"

response = requests.post(url=graph_post_endpoint, json=graph_params, headers=headers)
print(response.text)