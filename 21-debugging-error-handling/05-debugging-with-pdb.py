# debugging with pdb
# import pdb; pdb.set_trace() -> commonly invoked on a single line

import pdb

# Common pdb commands
# l (list)
# n (next line)
# p (print)
# c (continue - to finish/quit debugging)


first = "First"
second = "Second"
pdb.set_trace()
result = first + second

third = "Third"
result += third
print(result)
