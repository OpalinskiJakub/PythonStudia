line="Zadanie trzynaste z python"

splited_line=line.split()

amount=0

for word in splited_line:
    amount+=len(word)

print(f"Laczna dlogosc wyrazow w napisie:{amount}")