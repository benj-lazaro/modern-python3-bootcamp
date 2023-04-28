# Write a function called next_prime()
# It returns a generator that yields an unlimited number of primes
# Starting from the first prime = 2


def next_prime():
    """next_prime() returns a generator of primes starting at 2."""
    number = 2

    while True:
        is_prime = True

        for index in range(2, number):
            if number % index == 0:
                is_prime = False

        if is_prime:
            yield number

        number += 1


# Test Code
primes = next_prime()
prime_list = [next(primes) for i in range(25)]
print(prime_list)
