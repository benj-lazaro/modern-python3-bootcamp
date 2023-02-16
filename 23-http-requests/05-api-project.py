import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

URL = "https://icanhazdadjoke.com/search"

# Display program header
header_text = figlet_format("Dad Joke 3000")
header_text_color = colored(header_text, color="magenta")
print(header_text_color)

# User input
search_topic = str(input("Let me tell you a joke! Give me a topic: "))

# HTTP request
response = requests.get(
    URL,
    headers={"Accept": "application/json"},
    params={"term": search_topic, }
).json()

number_of_jokes = response['total_jokes']

# Process HTTP response
if number_of_jokes > 1:
    print(f"I've got {number_of_jokes} jokes about {search_topic}. Here's one.")
    print(choice(response['results'])['joke'])
elif number_of_jokes == 1:
    print(f"I've got one joke about {search_topic}. Here it is.")
    print(response['results'][0]['joke'])
else:
    print(f"Sorry, I don't have any jokes about {search_topic}! Please try again.")
