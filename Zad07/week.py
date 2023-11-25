from itertools import cycle,islice


def weekday_number_generator():
    return cycle(range(7))

iterator=weekday_number_generator()

expected=[0,1,2,3,4,5,6,0,1,2,3,4,5,6]
generated=list(islice(iterator, 14))
assert expected==generated , f"Expected{expected}"