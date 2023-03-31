import re

# Regex is grouped using a pair of ( )
url_pattern = r"(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)"

url_regex = re.compile(url_pattern)
match = url_regex.search("https://www.my-website.com/bio?data=who&mech=yes")

print(match.group(0))                           # Returns the entire matching string value
print(f"Protocol: {match.group(1)}")            # Returns the 1st group of the matching string value
print(f"Domain: {match.group(2)}")              # Returns the 2nd group
print(f"Everything Else: {match.group(3)}")     # Returns the 3rd group

# .groups() returns a tuple; items correspond to the groups / parenthesis defined in the regex pattern
# print(match.groups())
