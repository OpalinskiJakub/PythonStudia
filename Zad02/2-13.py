    
def length(line):


    splited_line=line.split()

    amount=0

    for word in splited_line:
        amount+=len(word)

    print(f"Laczna dlogosc wyrazow w napisie:{amount}")
    
    return amount

input="Zadanie trzynaste z python"
output=23

assert length(input)==output,f"Expected: {output}"