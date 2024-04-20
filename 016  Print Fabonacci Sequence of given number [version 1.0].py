# Print Fabonacci Sequence of given number [version 1.0]

def fabonacci(num):
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return (fabonacci(num - 1) + fabonacci(num - 2))

num = int(input(">>> "))
print(fabonacci(num))

# A quick quiz on recursion in functions
