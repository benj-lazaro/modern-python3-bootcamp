def say_sup():
    """say_sup() prints a string and the value of __name__."""
    print(f"Sup! My __name__ is {__name__}")


# To PREVENT the following code from being EXECUTED IMMEDIATELY after being imported
if __name__ == "__main__":
    say_sup()
