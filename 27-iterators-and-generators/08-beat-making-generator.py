# An infinite generator demo
# Yields a '1' then a '2' then a '3' then a '4' then returns to '1' & repeats the pattern indefinitely

def current_beat():
    """current_beat() returns numbers from 1 to 4 for each call w/ next(); resets back to 1 & starts over."""
    number_tuple = (1, 2, 3, 4)
    index_tuple = 0
    while True:
        if index_tuple >= len(number_tuple):
            index_tuple = 0

        yield  number_tuple[index_tuple]
        index_tuple += 1


# Test Code
beat = current_beat()
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
