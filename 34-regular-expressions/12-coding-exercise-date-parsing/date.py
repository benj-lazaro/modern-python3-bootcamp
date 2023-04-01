# Write a function called parse_date
# Accepts a single string
# Checks if the string matches a date format = dd/mm/yyyy or dd.nn.yyyy or dd,mm,yyyy
# Returns a dictionary containing the three parts with keys:
# d = date
# m = month
# y = year
# Use symbolic group names to label each section of the passed string

import re


def parse_date(string_input):
    """parse_date(str) returns a dictionary containing values of symbolic group names."""
    date_regex = re.compile(r"^(?P<date>\d{2})[,/.](?P<month>\d{2})[,/.](?P<year>\d{4})$")
    date_match = date_regex.search(string_input)

    if date_match:
        return {
            "d": date_match.group("date"),
            "m": date_match.group("month"),
            "y": date_match.group("year")
        }
    return None


print(parse_date("01/22/1999"))
print(parse_date("12,04,2003"))
print(parse_date("12.11.2003"))
print(parse_date("12.11.200312"))
