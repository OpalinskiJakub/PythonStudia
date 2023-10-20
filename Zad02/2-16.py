
def replace(line):
    replaced_line=line.replace("GvR","Guido van Rossum")

    print(f"Wynik:{replaced_line}")

    return replaced_line


input="Zadanie GvR szeGvRsnaste z pythona GvR"
output1="Zadanie Guido van Rossum szeGuido van Rossumsnaste z pythona Guido van Rossum"


assert replace(input)==output1,f"Expected: {output1}"