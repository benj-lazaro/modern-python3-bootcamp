# Substitution demo
# .sub() = 1st argument contains the replacement word, 2nd argument refers to the original string/text
# \g<group_number> = refers to a capture group where substitution will take place

import re

original_text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow."

pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) [a-z]+", re.I)         # (Mr\.|Mrs\.|Ms\.) = capture group 1
new_text = pattern.sub("\g<1> REDACTED", original_text)         # Substitute with 'Mr.|Mrs.|Ms. REDACTED'
print(new_text)

pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+", re.I)  # capture group 2 = 1st letter of each name
new_text = pattern.sub("\g<1> \g<2>", original_text)
print(new_text)
