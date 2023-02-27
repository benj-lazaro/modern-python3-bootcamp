# Create a custom iterator that simulates the range() function

class Counter:
    def __init__(self, low_value, high_value):
        self.current_value = low_value
        self.high_value = high_value

    def __iter__(self):
        """__iter__(self) overrides the built-in iter() function."""
        return self

    def __next__(self):
        """__next__(self) overrides the built-in next() function."""
        if self.current_value < self.high_value:
            number = self.current_value
            self.current_value += 1
            return number
        raise StopIteration


for current_number in Counter(50, 70):
    print(current_number)
