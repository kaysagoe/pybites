import random

names = ["Julian", "Bob", "PyBites", "Dante", "Martin", "Rodolfo"]
aliases = ["Pythonista", "Nerd", "Coder"] * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = " | "


def generate_table(*args):
    return [SEPARATOR.join([str(value) for value in row]) for row in zip(*args)]
