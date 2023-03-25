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
from random import choice
import requests

# Constant variable(s)
BASE_URL = "https://quotes.toscrape.com/"

# Global variable(s)
sleep_value = 2  # Pause between each web page being scrapped; measured in seconds


def scrape_quotes():
    all_quotes = []  # Store harvested data from the fetched HTML document
    url = "/page/1"  # Refers to the current page being processed

    while url:
        response = requests.get(f"{BASE_URL}{url}")  # Fetch the HTML document
        print(f"Now scraping {BASE_URL}{url}...")

        soup = BeautifulSoup(response.text, "html.parser")  # Parse the HTML document
        quote_block = soup.find_all(class_="quote")  # Fetch the element tag with class = 'quote'

        for quote in quote_block:  # Access required data & save as a dictionary to the list
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })

        next_button = soup.find(class_="next")  # Check for the existence of a 'Next Page' button
        url = next_button.find("a")["href"] if next_button else None  # Update url or terminate loop
        sleep(sleep_value)

    print("Scraping done...\n")
    sleep(sleep_value)
    return all_quotes


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    guess = ""

    print(quote["text"])
    print(quote["author"])  # For testing purposes only

    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = str(input(f"Who said this quote? Guesses remaining: {remaining_guesses} \n"))

        if guess.lower() == quote["author"].lower():
            print("You got it right!")
            break

        remaining_guesses -= 1

        if remaining_guesses == 3:
            response = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(response.text, "html.parser")

            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place}.")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author's first name starts with {quote['author'][0]}. ")
        elif remaining_guesses == 1:
            author_lastname_initial = quote["author"].split(" ")[1][0]  # Selects 2nd list item & it's 1st character
            print(f"Here's a hint: The author's last name starts with {author_lastname_initial}. ")
        else:
            print(f"Sorry, you ran out of guesses. The answer was {quote['author']}.")

    play_again = ""
    while play_again.lower() not in ("y", "yes", "n", "no"):
        play_again = str(input("Would you like to play again [y/n]? "))

    if play_again.lower() in ("yes", "y"):
        return start_game(quotes)
    else:
        print("Ok. Goodbye.")


quotes = scrape_quotes()
start_game(quotes)
