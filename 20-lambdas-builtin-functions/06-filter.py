# filter = there is a lambda for each value in the iterable
# Returns a filter object containing values that return True to the lambda
# The filter object can be converted into another data structure

# Iterate through the list items in the number_list, return even numbers
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = list(filter(lambda number: number % 2 == 0, number_list))
print(f"Iterable number_list: {number_list}")
print(f"filter object even_number: {even_number}")


# Iterate through the items in the name_list, return items starting with the letter 'a'
name_list = ["austin", "penny", "anthony", "angel", "billy"]
name_starting_with_a = list(filter(lambda name: name[0] == "a", name_list))
print(f"\nIterable name_list: {name_list}")
print(f"filter object name_starting_with_a: {name_starting_with_a}")

# Iterate through dictionary items in the list user_tweets, return items with empty tweets
user_tweets = [
    {"username": "Samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "Katie", "tweets": ["I love my cat"]},
    {"username": "Jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_lover", "tweets": ["Dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]
# To catch inactive users using len() on their tweets
inactive_accounts = list(filter(lambda user: len(user['tweets']) == 0, user_tweets))
print(f"\nIterable user_tweets: {user_tweets}")
print(f"filter object inactive_accounts: {inactive_accounts}")

# To catch inactive users using logical NOT on their tweets (Falsy values)
inactive_accounts = list(filter(lambda user: not user['tweets'], user_tweets))
print(f"filter object inactive_accounts: {inactive_accounts}")

# Return inactive user accounts ONLY using the combination of map and fiter
inactive_users = list(map(lambda user: user['username'], filter(lambda user: not user['tweets'], user_tweets)))
print(f"filter object inactive_users: {inactive_users}")

# List comprehension solution
inactive_accounts = [user for user in user_tweets if not user['tweets']]
print(f"List comprehension: {inactive_accounts}")

inactive_users = [user['username'] for user in user_tweets if not user['tweets']]
print(f"List comprehension: {inactive_users}")
