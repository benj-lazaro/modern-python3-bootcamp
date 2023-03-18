# Writing to CSV files using DictWriter
# Creates a writer object for writing to CSV files using dictionaries
# fieldnames = kwarg for DictWriter specifying the header row
# writeheader = method to write a line of headers
# writerow = method to write a row based on a dictionary

from csv import DictWriter

with open("example.csv", "w") as data:
    headers = ["Character", "Finishing Move"]       # Setup row headers
    content = DictWriter(data, fieldnames=headers)
    content.writeheader()                           # Write row headers
    content.writerow({                              # Write content per row in dictionary form
        "Character": "Ryu",
        "Finishing Move": "Hadouken"
    })
    content.writerow({
        "Character": "Ken",
        "Finishing Move": "Shoryuken"
    })
    content.writerow({
        "Character": "Chun-Li",
        "Finishing Move": "Kaitenteki Kakukyakushu"
    })


with open("cats.csv", "w") as data:
    headers = ["Name", "Breed", "Age"]
    content = DictWriter(data, fieldnames=headers)
    content.writeheader()
    content.writerow({
        "Name": "Blue",
        "Breed": "Scottish Fold",
        "Age": 3
    })
    content.writerow({
        "Name": "Kitty",
        "Breed": "Russian Blue",
        "Age": 1
    })
    content.writerow({
        "Name": "Garfield",
        "Breed": "Orange Tabby",
        "Age": 10
    })
