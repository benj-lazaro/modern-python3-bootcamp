# query string = key-value pairs passed to a server as part of a GET request
import requests

url = "https://icanhazdadjoke.com/search"

# Send HTTP request with params
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
)

data = response.json()
print(data['results'])
