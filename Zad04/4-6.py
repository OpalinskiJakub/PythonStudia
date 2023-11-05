def sum_seq(sequence):
    result=0
    for i in sequence:
        if isinstance(i,(list,tuple)):
            result=result+sum_seq(i)
        elif isinstance(i,(int,float)):
            result=result+i

    return result
    



input1=[1,(1,2),[13]]
result1=17

input2=[(5),5,[5],((5))]
result2=20

assert sum_seq(input1)==result1,f"Expected:{result1}"
assert sum_seq(input2)==result2,f"Expected:{result2}"
    