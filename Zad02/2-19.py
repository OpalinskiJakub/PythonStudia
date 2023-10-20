L=[1,2,3,343,33,234,12]
def bulid(L):
    numbers_with_zeros=[]

    for number in L:
        numbers_with_zeros.append(str(number).zfill(3))

    result="".join(numbers_with_zeros)

    print(f"Wynik:{result}")

    return result



input=[1,2,3,343,33,234,12]
output1="001002003343033234012"


assert bulid(input)==output1,f"Expected: {output1}"