# try-except-else block

def divide(dividend, divisor):
    try:
        quotient = dividend / divisor
    except ZeroDivisionError as error:
        print("Divisor is zero; please DO NOT divide by zero.")
        print(error)
    except TypeError as error:
        print("Divident & Divisor MUST be an int or float.")
        print(error)
    else:
        print(f"Result: {dividend} / {divisor} = {quotient}")


divide(2, 1)
divide(1, 0)
divide(1,'a')
divide('a', 2)
