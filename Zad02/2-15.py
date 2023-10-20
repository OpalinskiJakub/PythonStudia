
def create(L):
    Lstr=[]

    for digit in L:
        Lstr.append(str(digit))

    number_list="".join(Lstr)

    print(f"Wyraz z cyfr:{number_list}")

    return number_list

input=[1,13,43,43,23,12,32,432]
output1="1134343231232432"


assert create(input)==output1,f"Expected: {output1}"

