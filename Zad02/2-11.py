    
def separate(word):
   
    wordwithseparator="-".join(word)

    print(f"Wyraz z separatorem:{wordwithseparator}")

    return wordwithseparator

input="python"
output="p-y-t-h-o-n"

assert separate(input)==output,f"Expected: {output}"