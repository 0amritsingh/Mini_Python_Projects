# Multiplication Table Printer [version 1.3]

x = "Multiplication table printer"
print(x)
a = int(input("Enter your Number: "))
b = int(input("For how many times: "))
for i in range(1, b + 1): # start at 1 and srop at b+1
    print (a, "x", i, "=", a*i)
    