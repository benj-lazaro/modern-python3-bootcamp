# Swap items within a given string demo
# Reorganize books in a list s by swapping its publication date and title

import re


book_titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Baby cakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]

update_book_titles = []

# Sort book titles according to how they're stored in a list (book titles)
book_titles.sort()
print(book_titles)

# Define regex pattern; use capture groups to swap the publication date and titles of books
book_regex_pattern = re.compile(r"(^[\w ]+) \((\d{4})\)")

# Loop through each book title and save changes on a new list
for book in book_titles:
    result = book_regex_pattern.sub("\g<2> - \g<1>", book)
    update_book_titles.append(result)

# Sort and print the book titles using the new title format
update_book_titles.sort()
print(update_book_titles)
