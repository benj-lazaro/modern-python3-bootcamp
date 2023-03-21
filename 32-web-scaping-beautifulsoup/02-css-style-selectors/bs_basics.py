# BeautifulSoup basics
# Selecting using CSS style selectors using .select()
# .select() returns a list of matching elements; cleaner alternative to .find() and .find_all()

# Select by id = #foobar
# Select by class = .foobar
# Select by children = foo > bar
# Select by descendants = foo bar

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

# Select by id
print("Select matching elements by CSS selector id")
matching_elements = soup.select("#first")       # Returns matching element(s) enclosed in a list
print(matching_elements)
print("\n")

# Select the 1st matching element by ID
print("Select matching 1st element by CSS selector id:")
matching_elements = soup.select("#first")[0]    # Returns a specific matching element; no long enclosed in a list
print(matching_elements)
print("\n")

# Select by class
print("Select matching elements by CSS selector class:")
matching_elements = soup.select(".special")
print(matching_elements)
print("\n")

# Select by element
print("Select matching elements by element name:")
matching_elements = soup.select("div")
print(matching_elements)
print("\n")

# Select by attribute
print("Select matching elements by attribute:")
matching_elements = soup.select("[data-example]")
print(matching_elements)
print("\n")
