# doctests implementation using the TDD mindset (i.e. Red, Green, Refactor)
# NOTE: doctests expect a pair of '' to be returned and not "" on the result of the test
# NOTE: A trailing whitespace at the END of the test result can FAIL the test
# NOTE: The order of the keys in a dictionary DOES MATTER in doctests

def double(values):
    """ double(values) doubles the values in a list.

    >>> double([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]


def say_hi():
    """say_hi() simply returns a string.
    >>> say_hi()
    'hi'
    """
    return 'hi'


def true_that():
    """true_that() simply returns a True.
    >>> true_that()
    True
    """
    return True


def make_dict(keys):
    """
    >>> make_dict(['a', 'b'])
    {'a': True, 'b': True}
    """
    return {key: True for key in keys}

