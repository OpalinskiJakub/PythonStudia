
from itertools import islice

import random
directions = ["N", "E", "S", "W"]

class DirectionsIterator:
    def __init__(self):
        self.directions = ["N", "E", "S", "W"]

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.directions)



iterator = iter(DirectionsIterator())
generated = islice(iterator, 10) 
for value in generated:
    assert value in directions, f"Generated value '{value}' not in directions list"
