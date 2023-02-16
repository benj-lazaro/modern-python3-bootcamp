# Define a class called Comment
# It should have the following attributes:
# - username = username of the person
# - text = the actual comment
# - likes = number of likes (default = 0)

class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


# Instantiate Commenct class into objects & pass corresponding test argument values
comment_1 = Comment("rosa77", "Soooo cute!!!")
print(f"Comment: {comment_1.text}")
print(f"From: {comment_1.username}")
print(f"Like Count: {comment_1.likes}\n")

comment_2 = Comment("davey123", "lol you're silly", 3)
print(f"Comment: {comment_2.text}")
print(f"From: {comment_2.username}")
print(f"Like Count: {comment_2.likes}\n")
