# Reads the content of fighters.csv file
# Capitalize content of fighters.csv
# Write updated content to a new file called screaming_fighters.csv

from csv import reader, writer

with open("fighters.csv") as data:
    content = reader(data)
    fighters = [[fighter.upper() for fighter in row] for row in content]    # Save content as a list

with open("screaming_fighters-v1.csv", "w") as data:
    content = writer(data)

    for row in fighters:
        content.writerow(row)

    print("screaming fighters... done")
