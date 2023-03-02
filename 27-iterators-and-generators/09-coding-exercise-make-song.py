# Write a function called make_song
# Takes a count (int, default value of 99) and a beverage (string, default value of 'soda')
# Returns a generator object that yields a verse from a popular song about a beverage
# The number of verses in the song is determined by the count

def make_song(verse_count=99, beverage="soda"):
    """make_soing(int, str) returns a generator object returns a verse from a popular beverage song."""
    for number in range(verse_count, -1, -1):
        if number > 1:
            yield f"{number} bottles of {beverage} on the wall."
        elif number == 1:
            yield f"Only 1 bottle of {beverage} on the wall."
        else:
            yield f"No more {beverage}"


# Test Code
print("Test Code: passing user-defined argument values make_song()...")
number_of_bottles = 5
preferred_beverage = "rum"
capt_jack_sparrow_song = make_song(number_of_bottles, preferred_beverage)
for count in range(number_of_bottles + 1):
    print(next(capt_jack_sparrow_song))

print("\nTest Code: passing no argument values to make_song()....")
the_default_song = make_song()
for count in range(100):
    print(next(the_default_song))
