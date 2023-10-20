
def front(line):
    splited_line=line.split()

    front=[]

    for word in splited_line:
        front.append(word[0])
        

    word_from_front="".join(front)

    print(f"Napis stworzony z pierwszych znaków:{word_from_front}")

    return word_from_front

def back(line):
    splited_line=line.split()

    back=[]

    for word in splited_line:
        back.append(word[-1])

    word_from_back="".join(back)

    
    print(f"Napis stworzony z ostatnich znaków wyrazów:{word_from_back}")

    return word_from_back



input="Zadanie numer dwanascie python"
output1="Zndp"
output2="eren"

assert front(input)==output1,f"Expected: {output1}"
assert back(input)==output2,f"Expected: {output2}"