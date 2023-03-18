# Reads the content of fighters.csv file
# Capitalize content of fighters.csv
# Write updated content to a new file called screaming_fighters.csv
# Using nested with statements

from csv import reader, writer

with open("fighters.csv") as reader_data:
    read_content = reader(reader_data)

    with open("screaming_fighters-v2.csv", "w") as writer_data:
        write_content = writer(writer_data)

        for row in read_content:
            write_content.writerow([fighter.upper() for fighter in row])
