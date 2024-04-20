# Multiplication Table Printer [version 1.2]

x = "welcome to multiplication table printer"
print(x.title())
a = int(input("Enter your Number\n>>> "))
b = int(input("For how many times\n>>> "))

i = 1
while (i <= b):
    print (a, "x", i, "=", a*i)
    i = i + 1
    # i += 1
    