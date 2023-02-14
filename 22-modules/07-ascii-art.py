# ASCII art printer
from pyfiglet import figlet_format
from termcolor import colored

def print_art(message, color):
    """print_art(message, color) prints ASCII art in specified color."""
    official_termcolors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

    if color not in official_termcolors:
        color = 'magenta'

    ascii_art = figlet_format(message)
    colored_ascii = colored(ascii_art, color=user_color)
    print(ascii_art)


print("Welcome to ASCII Art Printer")
user_message = str(input("What would you like to print? "))
user_color = str(input("What color? "))
print_art(user_message, user_color)
