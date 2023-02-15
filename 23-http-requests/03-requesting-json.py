import requests

url = "https://icanhazdadjoke.com/"

# Request content in json format; returns as a string that looks like a dictionary
response = requests.get(url, headers={"Accept": "application/json"})

# Convert returned json content into a proper Python dictionary
data = response.json()

# Print the entire dictionary content
print(data)

# Print dictionary values using their corresponding keys
print(f"ID: {data['id']}")
print(f"Joke: {data['joke']}")
print(f"Status: {data['status']}")
