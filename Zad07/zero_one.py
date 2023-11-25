from itertools import islice

class ZeroOneIterator:
    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.index % 2
        self.index += 1
        return value
    
iterator=iter(ZeroOneIterator())

expected=[0, 1, 0, 1]
generated=list(islice(iterator,4))
assert expected==generated , f"Expected{expected}"
