import re


def extract_phone(string_input):
    """extract_phone(str) returns the first matching instance from the passed string."""
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")      # \b ensures an exact match to the pattern
    match = phone_regex.search(string_input)

    if match:
        return match.group()
    return None


def extract_all_phones(string_input):
    """extract_phone(str) returns all matching instances from the passed string as a list."""
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")      # \b ensures an exact match to the pattern
    match = phone_regex.findall(string_input)

    if match:
        return match
    return None


def is_valid_phone1(string_input):
    """is_valid_phone(str) returns True if the entire passed string is a phone number ONLY."""
    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")        # NOTHING comes before & after the phone number
    match = phone_regex.search(string_input)

    if match:
        return True
    return False


def is_valid_phone2(string_input):
    """is_valid_phone(str) returns True if the entire passed string is a phone number ONLY."""
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")      # Retains the same search pattern
    match = phone_regex.fullmatch(string_input)             # Scans for the exact match in the passed string

    if match:
        return True
    return False


# Test Code
print("Testing extract_phone()...")
print(extract_phone("My phone number is 123 456-7890."))
print(extract_phone("My other phone number is 890 765-432100."))
print(extract_phone("890 765-4321 is Haruna-san's phone number."))
print(extract_phone("123 456-7890"))

print("\nTesting extract_all_phones()...")
print(extract_all_phones("Call me at 123 456-7890 or 890 765-4321."))
print(extract_all_phones("123456789 this is a test string with no phone number"))

print("\nTesting is_valid()_phone()1...")
print(is_valid_phone1("123 456-7890"))
print(is_valid_phone1("Call me at 123 456-7890 or 890 765-4321."))
print(is_valid_phone1("890 765-4321 is Haruna-san's phone number."))

print("\nTesting is_valid()_phone()2...")
print(is_valid_phone2("123 456-7890"))
print(is_valid_phone2("Call me at 123 456-7890 or 890 765-4321."))
print(is_valid_phone2("890 765-4321 is Haruna-san's phone number."))
