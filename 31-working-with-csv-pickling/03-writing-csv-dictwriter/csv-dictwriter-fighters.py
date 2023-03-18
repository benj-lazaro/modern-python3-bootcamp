# Convert height of fighters from centimeters to inches
from csv import DictWriter, DictReader


def cm_to_inch(cm):
    """cm_to_inch(number) returns the converted and rounded centimeters to to inches."""
    return round(float(cm) * 0.393701)


with open("fighters.csv") as read_data:
    read_content = DictReader(read_data)
    fighters = list(read_content)

with open("fighters-inches.csv", "w") as write_data:
    headers = ("Name", "Country", "Height (in inches)")
    write_content = DictWriter(write_data, fieldnames=headers)
    write_content.writeheader()

    for fighter in fighters:
        write_content.writerow({
            "Name": fighter["Name"],
            "Country": fighter["Country"],
            "Height (in inches)": cm_to_inch(fighter["Height (in cm)"])
        })
