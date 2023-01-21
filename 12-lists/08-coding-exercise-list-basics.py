# Create a list called instructors
# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"

# Run the tests to make sure you've done this correctly!

# Using .append()
instructors = []
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")
print("Using .append() method:")
print(instructors)

# Using .extend()
instructors_spare = []
instructors_spare.extend(["Colt", "Blue", "Lisa"])
print("\nUsing .extend() method:")
print(instructors_spare)
