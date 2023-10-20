
def amount(line):
    splitted=line.split()

    amount=len(splitted)

    print(f"Ilosc wyrazow:{amount}")

    return amount

input="raz   dwa trzy \n cztery\tpie"
output=5

assert amount(input)==output,f"Expected: {output}"