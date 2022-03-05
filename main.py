import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "in_eu": response.get("in_eu"),
        "postal": response.get("postal"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "timezone": response.get("timezone"),
        "utc_offset": response.get("utc_offset"),
        "country_calling_code": response.get("country_calling_code"),
        "currency": response.get("currency"),
        "currency_name": response.get("currency_name"),
        "languages": response.get("languages"),
        "country_area": response.get("country_area"),
        "country_population": response.get("country_population")
    }
    return location_data


print(get_location())
