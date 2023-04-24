# Write a function called reverse_vowels()
# It accepts a string
# Reverse the existing vowels within the string
# Returns a new string containing with the vowels in reverse


def reverse_vowels(string_data):
    """reverse_vowels(str) returns a new string with vowels in reverse."""
    existing_vowels = [string_data[index] for index in range(len(string_data)) if string_data[index] in 'aeiouAEIOU']
    existing_vowels.reverse()
    vowel_counter = 0
    new_string = ''

    for index in range(len(string_data)):
        if string_data[index] in 'aeiouAEIOU':
            new_string += existing_vowels[vowel_counter]
            vowel_counter += 1
        else:
            new_string += string_data[index]

    return new_string


print(reverse_vowels("Hello!"))                         # Returns Holle
print(reverse_vowels("HELLO!"))                         # Returns HOLLE
print(reverse_vowels("Tomatoes"))                       # Returns Temotaos
print(reverse_vowels("Reverse Vowels In A String"))     # Returns RivArsI Vewols en e Streng
print(reverse_vowels("aeiou"))                          # Returns uoiea
print(reverse_vowels("AEIOU"))                          # Returns UOIEA
print(reverse_vowels("why try, shy fly?"))              # Returns why try, shy fly? (no vowels)
