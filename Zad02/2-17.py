line="Zadanie siedemnaste z pythona"

splited_line=line.split()

sorted_by_alphabet=sorted(splited_line)

sorted_by_lenght=sorted(splited_line,key=len)

print(f"Posortowane alfabetycznie:{sorted_by_alphabet}")

print(f"Posortowane pod dlugosci:{sorted_by_lenght}")