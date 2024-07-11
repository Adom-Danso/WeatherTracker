import requests

API = "2e3592173fd1f57f32acd5638573f5ff"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

def get_location_by_ip(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return data

def main():
	ip = get_public_ip()
	location_data = get_location_by_ip(ip)
	loc = location_data['loc'].split(',')
	latitude, longitude = loc[0], loc[1]

	request_url = f'{BASE_URL}?lat={latitude}&lon={longitude}&appid={API}'
	response = requests.get(request_url)

	if response.status_code == 200:
		data = response.json()
		weather = data['weather'][0]['description']
		temperature = round(data['main']['temp'] - 273.15, 2)
		print(f'Weather: {weather}')
		print(f'Temperature: {temperature}°C')
	else:
		print('An error occurred.')


if __name__ == "__main__":
    main()


https://ipinfo.io/8.8.8.8/json?token=46c23344eece2c{"hostname":"dns.google","city":"Mountain View","region":"California","country":"US","loc":"37.4056,-122.0775","postal":"94043","timezone":"America/Los_Angeles"}