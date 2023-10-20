line="Zadanie czternaste z pythona"

splited_line=line.split()

longest_word=max(splited_line,key=len)

lenght_longest=len(longest_word)

print(f"Najdluzszy wyraz:{longest_word}")
print(f"Dlogosc najdluzszego wyrazu:{lenght_longest}")

