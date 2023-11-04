def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

input1=15
result1=610

input2=9
result2=34

assert fibonacci(input1)==result1,f"Expected:{result1}"

assert fibonacci(input2)==result2,f"Expected:{result2}"