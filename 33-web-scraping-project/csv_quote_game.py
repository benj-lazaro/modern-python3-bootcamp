# Web Scraping Project = build a quotes guessing game

from bs4 import BeautifulSoup
from random import choice
from csv import DictReader
import requests

# Constant variable(s)
BASE_URL = "https://quotes.toscrape.com/"


def read_quotes(filename):
    """read_quotes(file) reads content of CSV file and return read data as a list."""
    with open(filename, "r", encoding="utf-8") as data:
        csv_reader = DictReader(data)
        return list(csv_reader)


def print_hint(quote, remaining_guesses):
    """print_hint(list, int) provides hints for the correct answer."""
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


def start_game(quotes):
    """start_game(list) read the passed list of imported quotes and starts the game."""
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
        print_hint(quote, remaining_guesses)

    play_again = ""
    while play_again.lower() not in ("y", "yes", "n", "no"):
        play_again = str(input("Would you like to play again [y/n]? "))

    if play_again.lower() in ("yes", "y"):
        return start_game(quotes)
    else:
        print("Ok. Goodbye.")


# start_game(quotes)
quotes = read_quotes("quotes.csv")
start_game(quotes)
