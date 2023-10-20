
def longest(line):
    splited_line=line.split()

    longest_word=max(splited_line,key=len)

    lenght_longest=len(longest_word)

    print(f"Najdluzszy wyraz:{longest_word}")
    print(f"Dlogosc najdluzszego wyrazu:{lenght_longest}")

    result=[longest_word,lenght_longest]

    return result




input="Zadanie czternaste z pythona"
output1=["czternaste",10]


assert longest(input)==output1,f"Expected: {output1}"
