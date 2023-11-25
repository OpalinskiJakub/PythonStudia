from itertools import islice


class WeekIterator:
    def __init__(self):
        self.day = 0

    def __iter__(self):
        return self

    def __next__(self):
        
        value = self.day % 7
        self.day += 1
        return value

iterator=iter(WeekIterator())

expected=[0,1,2,3,4,5,6,0,1,2,3,4,5,6]
generated=list(islice(iterator, 14))
assert expected==generated , f"Expected{expected}"