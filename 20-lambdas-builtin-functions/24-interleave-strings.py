# Write a function called interleave
# Accepts two strings
# Returns a new string containing 2 string interwoven together

def interleave(string1, string2):
    """interleave(str1, str2) returns a new string containing 2 string interwoven together."""
    # return ''.join(list(map(lambda string: ''.join(string), zip(string1, string2))))
    return ''.join(''.join(string) for string in zip(string1, string2))


print("Function: interleave()")
print(f"Documentation: {interleave.__doc__}")
print("\nStatmement: interleave('hi', 'ha')")
print(f"Result: {interleave('hi', 'ha')}")

print("\nStatmement: interleave('aaa', 'zzz')")
print(f"Result: {interleave('aaa', 'zzz')}")

print("\nStatmement: interleave('lzr','iad')")
print(f"Result: {interleave('lzr','iad')}")
