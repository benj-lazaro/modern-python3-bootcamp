# Web Scraping Project = build a quotes guessing game

# Program Requirements:
# 1. Grab data on every quote from https://quotes.toscrape.com/
# 2. Use requests and bs4 to get the data; grab the following and store it on a list
#    - text of the quote
#    - name of the person (who said the quote)
#    - href of the link (to the person's bio)
# 3. Display the quote to the user (player) and ask who said it; player will have 4 guesses
# 4. After each incorrect guess, the number of remaining guesses decrements
#    - remaining guesses = 0. the player loses
# 5. After each incorrect guess, the player receives a hint
#    - First hint = author's birthdate and location
#    - Succeeding hints = up to the developer
#      - 1st letter of the author's first or last name
#      - Number of letters of the author's first or last name
# 6. When the game is over, ask the player if they want to play again
#    - If yes, restart the game with a new quote
#    - if no, the program is complete (and terminates)

from bs4 import BeautifulSoup
from time import sleep
import requests

# Constant variable(s)
BASE_URL = "https://quotes.toscrape.com/"

# Global variable(s)
all_quotes = []     # Store harvested data from the fetched HTML document
sleep_value = 2     # Pause between each web page being scrapped; measured in seconds
url = "/page/1"     # Refers to the current page being processed

while url:
    response = requests.get(f"{BASE_URL}{url}")         # Fetch the HTML document
    print(f"Now scraping {BASE_URL}{url}...")

    soup = BeautifulSoup(response.text, "html.parser")  # Parse the HTML document
    quote_block = soup.find_all(class_="quote")         # Fetch the element tag with class = 'quote'

    for quote in quote_block:                           # Access required data & save as a dictionary to the list
        all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"]
        })

    next_button = soup.find(class_="next")                          # Check for the existence of a 'Next Page' button
    url = next_button.find("a")["href"] if next_button else None    # Update url or terminate loop
    sleep(sleep_value)

print("Scraping done...")
sleep(sleep_value)
print(all_quotes)
