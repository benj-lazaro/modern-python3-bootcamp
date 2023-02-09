# sorted = returns a new sorted list from the items in an iterable (besides... list)
# NOTE: source iterable untouched

number_list = [10, 4, 98, 34, 72, 1]
print(f"number_list: {number_list}")
print("Statement: sorted(number_list)")
print(f"Result: {sorted(number_list)}")
print("Statement: sorted(number_list, reverse=True)")
print(f"Result: {sorted(number_list, reverse=True)}")   # Reverse sort direction


number_tuple = (10, 4, 98, 34, 72, 1)
print(f"\nnumber_tuple: {number_tuple}")
print("Statement: sorted(number_tuple)")
print(sorted(number_tuple))
print("Statement: sorted(number_tuple, reverse=True)")
print(sorted(number_tuple, reverse=True))               # Reverse sort direction


user_dictionary = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_lover", "tweets": ["Dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]
print(f"\nuser_dictionary: {user_dictionary}")
print("Statement: sorted(user_dictionary, key=lambda user: user['username'])")
print(f"Result: {sorted(user_dictionary, key=lambda user: user['username'])}")
print("\nStatement: sorted(user_dictionary, key=lambda user: user['username'], reverse=True)")
print(f"Result: {sorted(user_dictionary, key=lambda user: user['username'], reverse=True)}")
print("\nStatement: sorted(user_dictionary, key=lambda user: len(user['tweets']))")
print(f"Result: {sorted(user_dictionary, key=lambda user: len(user['tweets']))}")
print("\nStatement: sorted(user_dictionary, key=lambda user: len(user['tweets']), reverse=True)")
print(f"Result: {sorted(user_dictionary, key=lambda user: len(user['tweets']), reverse=True)}")


songs_list = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]
print(f"\nsong_list: {songs_list}")
print("Statement: sorted(songs_list, key=lambda song: song['playcount'], reverse=True)")
print(f"Result: {sorted(songs_list, key=lambda song: song['playcount'], reverse=True)}")
