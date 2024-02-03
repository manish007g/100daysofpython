import requests
import datetime
MY_LAT = 12.971599
My_LONG = 77.594566
parameters = {
    "lat": MY_LAT,
    "lng": My_LONG,
    "formatted": 0,
    "tzid": "Asia/Kolkata"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
dt = datetime.datetime
time_now = dt.now()

print(time_now.hour)