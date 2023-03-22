# First Scraping Program
# Goals:
# Grab all links from the blog site (https://www.rithmschool.com/blog)
# Store the URL, anchor tag text and data to a CSV file

from bs4 import BeautifulSoup
from csv import writer
import requests

TARGET_URL = "https://www.rithmschool.com/blog"

# Access the target blog / website
response = requests.get(TARGET_URL)

# Instantiate BeautifulSoup & parse the fetched HTML page
soup = BeautifulSoup(response.text, "html.parser")

# Find all <article> elements
articles = soup.find_all("article")

# Prepare CSV file
with open("blog_data.csv", "w") as data:
    write_content = writer(data)
    csv_headers = ["Title", "Link", "Date"]
    write_content.writerow(csv_headers)

    # Loop through each article & fetch needed information
    for article in articles:
        article_tag = article.find("a")             # Access the <article> tag
        title = article_tag.get_text()              # Access the text of the <article> tag
        url = article_tag["href"]                   # Access the <href> tag
        date = article.find("time")["datetime"]     # Access the <time> tag & attribute 'datetime'
        write_content.writerow([title, url, date])  # Write each accessed data into a row of the CSV file
