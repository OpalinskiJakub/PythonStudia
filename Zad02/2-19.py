L=[1,2,3,343,33,234,12]

numbers_with_zeros=[]

for number in L:
    numbers_with_zeros.append(str(number).zfill(3))

result="".join(numbers_with_zeros)

print(f"Wynik:{result}")