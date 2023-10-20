
def sort(line):
    splited_line=line.split()

    sorted_by_alphabet=sorted(splited_line)

    sorted_by_lenght=sorted(splited_line,key=len)

    print(f"Posortowane alfabetycznie:{sorted_by_alphabet}")

    print(f"Posortowane pod dlugosci:{sorted_by_lenght}")

    result=[sorted_by_alphabet,sorted_by_lenght]

    return result



input="Zadanie siedemnaste z pythona"
output1=[['Zadanie', 'pythona', 'siedemnaste', 'z'],['z', 'Zadanie', 'pythona', 'siedemnaste']]


assert sort(input)==output1,f"Expected: {output1}"