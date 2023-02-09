# max() = return the largest item in an iterable / largest of the two or more arguments
# min() = return the smallest item in an iterable / smallest of the two or more arguments

number_list = [3, 4, 1, 2]
number_tuple = (1, 2, 3, 4)
string_data = "awesome"
dictionary_data = {
    1: 'a',
    3: 'c',
    2: 'b'
}

print(f"number_list: {number_list}")
print("Statement: max(number_list)")
print(f"Result: {max(number_list)}")
print("Statement: min(number_list)")
print(f"Result: {min(number_list)}")

print(f"\nnumber_tuple: {number_tuple}")
print("Statement: max(number_tuple)")
print(f"Result: {max(number_tuple)}")
print("Statement: min(number_tuple)")
print(f"Result: {min(number_tuple)}")

print(f"\nstring_data: {string_data}")
print("Statement: max(string_data)")
print(f"Result: {max(string_data)}")
print("Statement: min(string_data)")
print(f"Result: {min(string_data)}")

print(f"\ndictionary_data: {dictionary_data}")
print("Statement: max(dictionary_data)")
print(f"Rsult: {max(dictionary_data)}")
print("Statement: min(dictionary_data)")
print(f"Rsult: {min(dictionary_data)}")

name_list = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]
print(f"\nname_list: {name_list}")

print("Stateement: min(name_list, key=lambda name: len(name))")
shortest_name = min(name_list, key=lambda name: len(name))
print("Statement: max(name_list, key=lambda name: len(name))")
longest_name = max(name_list, key=lambda name: len(name))
print(f"Shortest name: {shortest_name}")
print(f"Longest name: {longest_name}")


songs_list = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(f"\nsongs_list: {songs_list}")
print("Statement: min(songs_list, key=lambda song: song['playcount'])['title']")
least_playcount = min(songs_list, key=lambda song: song['playcount'])['title']
print(f"Least playcount song: {least_playcount}")

print("\nStatement: max(songs_list, key=lambda song: song['playcount'])['title']")
most_playcount = max(songs_list, key=lambda song: song['playcount'])['title']
print(f"Most playcount song: {most_playcount}")
