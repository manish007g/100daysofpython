import requests
from twilio.rest import Client

API_KEY= "0d47e5debe22548b5eda8298a3b69e52"
LAT = 3.763386
LONG = 103.220184
account_sid = 'ACc42850297f530347f585718ccf09b264'
auth_token = 'ed03725ac16f8ccfb063f735e7a93de7'

parameters= {
    "lat": LAT,
    "lon": LONG,
    "cnt": 6,
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()

# data_code = data["list"][0]["weather"][0]["id"]

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:


    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="It's going to rain today. Remember to bring an Umbrella!!.",
                         from_='+12034429630',
                         to='+918605698837'
                     )

    print(message.status)

# print(data)