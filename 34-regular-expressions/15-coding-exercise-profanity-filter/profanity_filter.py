# Write a function called censor()
# Accepts a single string
# Censor made-up profane words = frack, fracking, fracker
# Substitute profane words with CENSORED

import re


def censor(string_input):
    """censor(str) returns a new string containing 'CENSORED' on profane words."""
    profane_regex = re.compile(r"\bfrack\w*\b", re.I)
    return profane_regex.sub("CENSORED", string_input)


# Test Code
print(censor("Frack you"))
print(censor("I hope you fracking die"))
print(censor("you fracking Frack"))
