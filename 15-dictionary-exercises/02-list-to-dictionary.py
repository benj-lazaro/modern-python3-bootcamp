# Given a variable called person
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# Create a dictionary called answer
# That makes each 1st item of the list as key and 2nd item as value
answer = {person[index][0]:person[index][1] for index in range(0, len(person))}
print(f"Answer: {answer}")
