from colorama import init
from termcolor import colored

init()
text = colored("Hi there", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)
