def sumSeq(seq):
    result=[]
    
    for i in seq:
        x=sum(i)
        result.append(x)
        
    return result

input=[[],[4],(1,2),[3,4],(5,6,7)]
expected=[0,4,3,7,18]
result=sumSeq(input)
assert result==expected,f"Expected:{expected}"

print(result)