# Reading CSV file using reader() of the CSV module
# Iterate over rows of the CSV and returns as an iterator (w/c you can go over it once)
# Each row is represented as a list
# Individual data is accessed via index value (see example below)
# CSV header will be included in the returned list but can be excluded using next()

from csv import reader

with open("fighters.csv") as data:
    csv_reader = reader(data)
    next(csv_reader)                        # Skips CSV file header row since it is an iterator

    for row in csv_reader:
        print(f"{row[0]} is from {row[1]}")


print("\n")
# To convert returned iterator into a list
with open("fighters.csv") as data:
    csv_reader = reader(data)
    list_data = list(csv_reader)
    print(list_data)
