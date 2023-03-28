# Scraping program
# Scrapes data from targeted URL

from bs4 import BeautifulSoup
from time import sleep
from random import choice
from  csv import DictWriter
import requests

# Constant variable(s)
BASE_URL = "https://quotes.toscrape.com/"

# Global variable(s)
sleep_value = 2  # Pause between each web page being scrapped; measured in seconds


def scrape_quotes():
    """scrape_quotes() collect selected data from targeted URL."""
    all_quotes = []  # Store harvested data from the fetched HTML document
    url = "/page/1"  # Refers to the current page being processed

    while url:
        response = requests.get(f"{BASE_URL}{url}")
        print(f"Now scraping {BASE_URL}{url}...")

        soup = BeautifulSoup(response.text, "html.parser")
        quote_block = soup.find_all(class_="quote")                   # Find element tags w/ class = 'quote'

        for quote in quote_block:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })

        next_button = soup.find(class_="next")                        # Checks for the 'Next Page' button
        url = next_button.find("a")["href"] if next_button else None  # Update url or break the loop
        sleep(sleep_value)                                            # Pause (in seconds) between scrapes

    print("Scraping done...\n")
    return all_quotes


def write_quotes(quotes):
    """write_quotes(list) write collected data into a CSV file."""
    with open("quotes.csv", "w", encoding="utf-8") as data:
        headers = ["text", "author", 'bio-link']
        csv_writer = DictWriter(data, fieldnames=headers)
        csv_writer.writeheader()

        for quote in quotes:
            csv_writer.writerow(quote)

        print("Saving into CSV file complete...")


# Write scrapped data into a CSV file
quotes = scrape_quotes()
write_quotes(quotes)
