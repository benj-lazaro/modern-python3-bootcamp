# SyntaxError = interpreter encounters an incorrect syntax
def first:      # forget parenthesis after function name
    pass


None = 1        # assigning a value to another value
return          # invoked without returning a value back to the calling program


# NameError = a variable that is NOT defined
test            # no value assigned to variable test


# TypeError = an operation or function applied to the wrong data type
len(5)          # int has NO len()

"awesome" + []  # can NOT concatenate a string with a list object


# IndexError = accessing an element in an iterable or sequence using an invalid index
list_data = ['hello']   # list has 1 item
list_data[2]            # accessing the non-existent 2nd item

tuple_data = (1,2,3,4)  # tuple has 4 items
tuple_data[6]           # accessing the non-existent 6th item


# ValueError = built-in operation or function receives the correct type but inappropriate value
int("foo")              # can NOT convert a string value into an integer; invalid literal


# KeyError = a dictionary that does NOT have the specific key
d = {}
d['foo']                # key 'foo' does NOT exists within the dictionary d


# AttributeError = a variable does NOT have an attribute
"awesome".foo           # string 'awesome' has no attribute 'foo'
[1, 2, 3].hello()       # list has no attribute 'hello'
"".joint(['a', 'b'])    # list has no attribute 'joint'

