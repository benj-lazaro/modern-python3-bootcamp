# BeautifulSoup basics

from bs4 import BeautifulSoup

# Navigating via tags using attributes:
# - parent / parents
# - contents
# - next_sibling / next_siblings
# - previous_sibling / previous_siblings

# Mockup HTML file inside a multi-lined string
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

# Setup BeautifulSoup to read the mockup HTML content and parse the content using html.parser
soup = BeautifulSoup(html, "html.parser")

# Select the <body> tag & its corresponding content; returns a list that includes '\n' characters
parent_tag = soup.body.contents
print("Access the parent <body> tag & contents:")
print(parent_tag)
print("\n")

# Select the <body> tag, access its first child & its corresponding content
first_child = soup.body.contents[1]
print("Access the first child & contents:")
print(first_child)
print("\n")

# Select the next sibling & its corresponding content
next_sibling = soup.body.contents[1].next_sibling.next_sibling  # Skips the '\n' between sibling tags
print("Access the next Sibling & contents:")
print(next_sibling)
print("\n")

# Select the parent tag (i.e. <ol> tag) of the 1st <li> tag with class = 'super-special'
parent_tag = soup.find(class_="super-special").parent
print("Access the parent tag & content of the 1st <li> with class = 'super-special':")
print(parent_tag)
print("\n")


# Navigating via searching using methods:
# - find_parent() / find_parents()
# - find_next_sibling() / find_next_siblings()
# - find_previous_sibling() / find_previous_siblings()
# NOTE: The aforementioned methods disregard the '\n' character embedded in-between element tags

# Find & access the next sibling of the element tag with an id = 'first'
print("Find & access the next sibling of the element tag with an id = 'first':")
matching_element = soup.find(id="first").find_next_sibling()
print(matching_element)
print("\n")

# Find & access the following next sibling of the previous selected element tag
print("Find & access the following next sibling of the previous selected element tag:")
matching_element = soup.find(id="first").find_next_sibling().find_next_sibling()
print(matching_element)
print("\n")

# Find & access the previous sibling of the last element tag with attribute 'data-example'
print("Find & access the previous sibling of the last element tag with attribute 'data-example':")
matching_element = soup.select("[data-example]")[1].find_previous_sibling()
print(matching_element)
print("\n")

# Find & access the sibling element tag with class = 'special' of the selected element with class = 'super-special'
print("Find & access the sibling element tag with class = 'special' of the selected element with class = "
      "'super-special'")
matching_element = soup.find(class_="super-special").find_next_sibling(class_="special")
print(matching_element)
print("\n")

# Find & access the parent element tag of the selected element <h3>
print("Find & access the parent element tag of the selected element <h3>:")
matching_element = soup.find("h3").find_parent()
print(matching_element)
print("\n")

# Find & access the parent element tag <html> of the selected element <h3>
print("Find & access the parent element tag <html> of the selected element <h3>:")
matching_element = soup.find("h3").find_parent("html")
print(matching_element)
print("\n")
