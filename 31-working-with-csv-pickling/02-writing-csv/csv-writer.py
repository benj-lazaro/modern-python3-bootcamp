# Writing to CSV using writer()
# writer() creates a writer object for writing content to a CSV file
# writerow() method writes a row (of content in the form of a list) to a CSV file

from csv import writer

with open("cats.csv", "w") as file:
    content = writer(file)
    content.writerow(["Name", "Age"])
    content.writerow(["Blue", 3])
    content.writerow(["Kitty", 1])
