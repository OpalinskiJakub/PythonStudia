from itertools import cycle,islice

def zero_one_iterator():
    return cycle([0, 1])


iterator=zero_one_iterator()

expected=[0, 1, 0, 1]
generated=list(islice(iterator,4))
assert expected==generated , f"Expected{expected}"
