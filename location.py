import requests
import json

phone_number = '7385272993'  # Replace with the phone number you want to trace

# Get cell tower information for the phone number
url = f'https://opencellid.org/lbs/json/locate?key=YOUR_API_KEY&cellid=0&lac=0&mcc=0&mnc=0&format=json&msisdn={phone_number}'
response = requests.get(url)
data = json.loads(response.text)

# Extract the latitude and longitude from the response
if 'lat' in data and 'lon' in data:
    latitude = data['lat']
    longitude = data['lon']
    print(f'Latitude: {latitude}, Longitude: {longitude}')
else:
    print('Could not retrieve location information')
