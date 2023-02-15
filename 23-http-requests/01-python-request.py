import requests

response = requests.get("https://news.ycombinator.com/")
print(f"Response code: {response}")
print(f"Response ok: {response.ok}")
print(f"Response header: {response.headers}")
print(f"Response text: {response.text}")
