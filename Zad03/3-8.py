def sumSet(seq1,seq2):
    result=list(set(seq1)|set(seq2))
    return result

def comSet(seq1,seq2):
    result=list(set(seq1)&set(seq2))
    return result

input1=[1,1,3,3,5,6]
input2=[1,1,3,3,5,6,7,8,9,9]
expectedSum=[1,3,5,6,7,8,9]
expectedCom=[1,3,5,6]

result1=sumSet(input1,input2)
result2=comSet(input1,input2)

assert result1==expectedSum,f"Expected:{expectedSum}"

print(result1)

assert result2==expectedCom,f"Expected:{expectedCom}"

print(result2)

