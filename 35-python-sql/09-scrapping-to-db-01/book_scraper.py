# Boot scraper = scrapes & sanitize data from website and save it to sqlite3 database

# import sqlite3
import requests
from bs4 import BeautifulSoup


def scrape_books(url):
    """scrape_books(url) retrieves targeted data from scrapped web page."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")

    all_books = []

    for book in books:
        # Get individual title, price & rating; save individual tuple as an item in a list
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)

    # Test Code
    print(all_books)


def get_title(book):
    """get_title(list) returns the book title"""
    return book.find("h3").find("a")["title"]


def get_price(book):
    """get_price(list) returns the book price and removes the corresponding currency symbol."""
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("£", "").replace("Â", ""))  # Remove currency symbol & convert to float


def get_rating(book):
    """get_rating(list) returns the book rating and coverts the star rating into a numerical value."""
    ratings = {
        "Zero": 0,
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    paragraph = book.select(".star-rating")[0]                  # Get book rating from scrapped data
    word_rating = paragraph.get_attribute_list("class")[-1]     # Last item (rating) in the list
    return ratings[word_rating]                                 # Convert to numerical rating


# Scrapes data from the targeted web page
scrape_books("http://books.toscrape.com/catalogue/category/books/history_32/index.html")
