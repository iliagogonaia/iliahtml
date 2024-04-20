import requests

DEMO_KEY = "1zE6EHiHd689FCUqrGjbeItT2B7Kj0OjhShNZ9oz"

url = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"

responce = requests.get(url)

print(responce.json())


