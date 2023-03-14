# Functions to be tested using unittest
from random import choice


def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):  # Checks if value of is_healthy is a boolean
        raise ValueError("is_healthy MUST be a boolean.")

    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"

    return f"I'm eating {food}, {ending}"


def nap(num_hours):
    if num_hours >= 2:
        return f"Ugh I overslept. I didn't mean to nap {num_hours} hours."

    return f"I'm feeling refreshed after my {num_hours} hour nap."


def is_funny(person):
    if person == "tim":
        return False

    return True


def laugh():
    return choice(('lol', 'haha', 'tehehe'))
