# Regex symbolic group name demo

import re


def parse_names(input_string):
    """parse_names(str) prints different parts of the passed string as values to assigned regex groups."""

    # NOTE: ?P<symbolic_group_name> = servers as a symbolic group name to the assigned regex group
    name_regex = re.compile(r'^(?P<title>Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = name_regex.search(input_string)

    print(matches.group())
    print(matches.group("title"))
    print(matches.group("first"))
    print(matches.group("last"))


# Test Code
parse_names("Mrs. Tilda Swinton")
