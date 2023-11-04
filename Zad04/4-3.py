def factorial(n):
    if n < 0:
        return None  
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


input1=5
result1=120

input2=10
result2=3628800

assert factorial(input1)==result1,f"Expected:{result1}"

assert factorial(input2)==result2,f"Expected:{result2}"