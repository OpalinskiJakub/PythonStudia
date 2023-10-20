line="Zadanie numer dwanascie python"

splited_line=line.split()

front=[]
back=[]

for word in splited_line:
    front.append(word[0])
    back.append(word[-1])

word_from_front="".join(front)
word_from_back="".join(back)



print(f"Napis stworzony z pierwszych znaków:{word_from_front}")
print(f"Napis stworzony z ostatnich znaków wyrazów:{word_from_back}")