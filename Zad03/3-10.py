

def roman2int(numbers,romanNumbers):
    result = 0
    left = 0
    
    for numeral in reversed(numbers):
        value = romanNumbers.get(numeral, 0)
        if value < left:
            result=result-value
        else:
            result=result+value
        left = value
    
    return result



romanNumbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

romanNumbers2 = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])


romanNumbers3 =  dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]))

input1="XXI"
input2="MX"
input3="VII"
expected1=21
expected2=1010
expected3=7

assert roman2int(input1,romanNumbers)==expected1,f"Expected:{expected1}"
assert roman2int(input2,romanNumbers2)==expected2,f"Expected:{expected2}"

assert roman2int(input3,romanNumbers3)==expected3,f"Expected:{expected3}"




