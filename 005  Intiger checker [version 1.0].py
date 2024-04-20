# Intiger checker [version 1.0]

a = int(input("Know your number is Positive or Negitive or Zero\nEnter your number: "))

if(a < 0):
    print(a, "is a Negitive Number")
elif(a == 0):
    print(a, "is Zero")
elif(a > 0):
    print(a, "is a Positive Number")
else:
    print("Invalid Data type. Please enter a Ingeter")