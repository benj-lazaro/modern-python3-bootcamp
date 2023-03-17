# Reading CSV file with DictReader() of the CSV module
# Iterate over rows of the CSV and returns as an itereator (w/c you can go over it once)
# Each row is represented as an ordered dictionary (OrderedDict)
# The CSV headers is automatically setup as a dictionary keys
# Individual data is accessed via name of the dictionary key

from csv import DictReader

with open("fighters.csv") as data:
    csv_reader = DictReader(data)

    for row in csv_reader:
        print(f"{row['Name']} is from {row['Country']}")
