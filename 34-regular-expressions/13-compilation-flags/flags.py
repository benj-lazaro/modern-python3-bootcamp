# Compilation flags demo
# DOTALL or S       = match any characters including newlines
# IGNORECASE or I   = case-insensitive matches
# VERBOSE or X      = enables a multi-lined regex pattern definition

import re

# email_regex = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

# Compilation flag VERBOSE allows a multi-lined regex pattern definition
# Use logical OR (|) to allow two or more compilation flags to be used simultaneously
email_verbose_regex = re.compile(r"""
    ^([a-z0-9_\.-]+)        # email user account
    @                       # single @ sign
    ([0-9a-z\.-]+)          # email providero
    \.                      # single . sign
    ([a-z\.]{2,6})$         # top domain name
""", re.VERBOSE | re.IGNORECASE)

match = email_verbose_regex.search("thomas123@yahoo.com")
print(match.group())
print(match.groups())

# Passed string shouldn't return as matched since the regex pattern did not include uppercase letters
# Using the compilation flag IGNORECASE, disregards the passed string's uppercase characters
match = email_verbose_regex.search("THOMAS123@YAHOO.COM")
print(match.group())
print(match.groups())
