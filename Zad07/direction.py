import random
from itertools import islice

directions = ["N", "E", "S", "W"]

def random_direction_iterator():
    while True:
        yield random.choice(directions)
        



iterator = random_direction_iterator()
generated_values = islice(iterator, 10) 
for value in generated_values:
    assert value in directions, f"Generated value '{value}' not in directions list"
