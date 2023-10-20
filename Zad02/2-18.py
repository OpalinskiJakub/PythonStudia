
def getAmount(number):
    number_to_str=str(number)

    amount=number_to_str.count("0")

    print(f"Ilosc zer:{amount}")
    
    return amount


input=404304030240
output1=5


assert getAmount(input)==output1,f"Expected: {output1}"