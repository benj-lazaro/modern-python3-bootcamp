# BeautifulSoup basics
# BeautifulSoup parses the HTML but DOES NOT download HTML
# It requires the requests module to access the targeted website

from bs4 import BeautifulSoup

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
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

# Setup BeautifulSoup to read the mockup HTML content and parse the content using html.parser
# Returns an object instantiated from class bs4.BeautifulSoup that contains the contents of the parsed HTML file
soup = BeautifulSoup(html, "html.parser")

# Display the content within the HTML <body> tag
print("Print the parsed <body> tag")
print(soup.body)
print("\n")

# Display the 1st <div> within the <body>
print("Print the 1st occurrence of <div>")
print(soup.body.div)
print("\n")

# Find the 1st occurrence of <div> using .find()
# Returns an element tag instance of the HTML element being searched for
print("Print the 1st occurrence of <div> using .find()")
matching_element = soup.find("div")
print(matching_element)
print("\n")

# Find all occurrences of <div> using .find_all()
# Returns a list containing matching items found
print("Print the all occurrences of <div> using .find_all()")
matching_elements = soup.find_all("div")
print(matching_elements)
print("\n")

# Find all occurrences of <li> using .find_all()
print("Print the all occurrences of <li> using .find_all()")
matching_elements = soup.find_all("li")
print(matching_elements)
print("\n")

# Find and select an elemental tag based on its assigned ID attribute
# Select element tag with an attribute ID of 'first'
print("Print the 1st occurrence of an elemental tag with the ID attribute 'first' using find()")
matching_element = soup.find(id="first")
print(matching_element)
print("\n")

# Find all occurrences of an elemental tag based on its assigned class attribute
# NOTE: Use 'class_' since 'class' is a reserved Python keyword
print("Print the all occurrence of an elemental tag with the class attribute 'class' using find_all()")
matching_elements = soup.find_all(class_="special")
print(matching_elements)
print("\n")

# Find all occurrence of an elemental tag based on its user-defined attributes & assigned value
# NOTE: Use 'attrs' and assign the user-defined attribute & it's assigned value as a dictionary
print("Print all occurrences of an element tag with the user-defined attribute of 'data-example' & assigned value.")
matching_elements = soup.find_all(attrs={"data-example": "yes"})
print(matching_elements)
print("\n")
