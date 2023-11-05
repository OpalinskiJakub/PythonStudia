def flatten(sequence):
    result=[]
    for i in sequence:
        if isinstance(i,(tuple,list)):
            result.extend(flatten(i))
        elif isinstance(i,(int,float)):
            result.append(i)
            
    return result

input1=[(1,(2)),[1],[[[3,[3]]]]]
result1=[1,2,1,3,3]
input2=[[[[[[[1]]]]]],(23),((2),((4)))]
result2=[1,23,2,4]
input3=[1,(2,3),[],[4,(5,6,7)],8,[9]]
result3=[1,2,3,4,5,6,7,8,9]
assert flatten(input1)==result1,f"Expected:{result1}"
assert flatten(input2)==result2,f"Expected:{result2}"
assert flatten(input3)==result3,f"Expected:{result3}"
