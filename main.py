import requests
from datetime import datetime
import smtplib

my_email = "m_stocker79@hotmail.com"
password = "Goku7986@"



my_lat = 43.996460
my_long = -92.445230
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()


longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (latitude, longitude)
print(iss_position)

parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0,
}
def is_overhead():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now().hour


if latitude > 40 and latitude < 46 and my_long-5<= longitude <= my_long+5:
    if time_now > 10:
        connection = smtplib.SMTP("smtp.live.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email, msg="Subject: Look up at ISS \n\n go outside and look for the iss.")
