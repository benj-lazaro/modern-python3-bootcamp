inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
print(f"inventory: {inventory}")

# Make a copy of inventory and save it to a variable called stock_list
print("\nCopy items of dictionary inventory into dictionary stock_list")
stock_list = {}
stock_list.update(inventory)
print(f"inventory: {inventory}")
print(f"stock_list: {stock_list}")

# add the value 18 to stock_list under the key "cookie"
print("\nAdd item 'cookie: 18' into the dictionary stock_list")
stock_list['cookie'] = 18
print(f"stock_list: {stock_list}")

# remove 'cake' from stock_list USE A DICTIONARY METHOD
print("\nRemove key 'cake' from dictionary stock_list")
stock_list.pop('cake')
print(f"stock_list: {stock_list}")
