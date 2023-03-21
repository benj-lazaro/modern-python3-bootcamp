# BeautifulSoup basics
# Accessing data from the parsed HTML file
# .get_text() = a method that access the inner text of a selected element
# .name = returns matching element's tag name
# .attrs= returns a dictionary of attributes assigned to the matching element

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
soup = BeautifulSoup(html, "html.parser")

# Select the 1st element with class 'special' & print corresponding inner text
print("Select the 1st element with class 'special' & print corresponding inner text:")
matching_element = soup.select(".special")[0]
print(matching_element.get_text())
print("\n")

# Print matching elements with class 'special'; get corresponding element name, inner text & attributes
print("Print matching elements with class 'special'; get corresponding element name, inner text & attributes:")
for matching_element in soup.select(".special"):
    print(f"Element Name: {matching_element.name}")
    print(f"Inner Text: {matching_element.get_text()}")
    print(f"Attributes: {matching_element.attrs}")
print("\n")

# Find matching <h3> element with attribute of 'data-example' & access it's assigned value
print("Find matching <h3> element with attribute of 'data-example' & access it's assigned value:")
matching_element = soup.find("h3")["data-example"]
print(matching_element)
print("\n")

# Find matching <div> element and access the assigned value to it's id attribute
print("Find matching <div> element and access the assigned value to it's id attribute:")
matching_element = soup.find("div")["id"]
print(matching_element)
print("\n")
