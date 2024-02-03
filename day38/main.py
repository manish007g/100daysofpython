import requests

GENDER = "MALE"
WEIGHT_KG = 76
HEIGHT_CM = 171
AGE = 31

query = input("Tell me which exercises you did :")

APP_ID = "5436aef0"
APP_KEY = "a6e63d49af5a9a75c5ba9dc28254c353"

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
  "query": query,
  "gender": GENDER,
  "weight_kg": WEIGHT_KG,
  "height_cm": HEIGHT_CM,
  "age": AGE
}


headers= {
  'x-app-id': APP_ID,
  'x-app-key': APP_KEY
}

response = requests.post(url=api_endpoint, data=params, headers=headers)
result = response.json()
print(result)