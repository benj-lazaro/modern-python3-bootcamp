# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!

# Use a for loop to sum up all donations
# Store the resulting sum in a variable called total_donations
total_donations = 0

for donation in donations.values():
    total_donations += donation

print(f"Total donations: {total_donations}")
