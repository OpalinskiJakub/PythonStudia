def odwracanie(L, left, right):
    if left < 0 or right <0 or right >= len(L) or left >= right:
        return  

    if left < right:
        L[left], L[right] = L[right], L[left]  
        odwracanie(L, left + 1, right - 1) 
        
input1=[1,4,3,2,5]
input2=[3,4,5,3,2]
odwracanie(input1,1,3)
odwracanie(input2,0,4)
result1=[1,2,3,4,5]
result2=[2,3,5,4,3]

assert input1==result1,f"Expected:{result1}"
assert input2==result2,f"Expected:{result2}"