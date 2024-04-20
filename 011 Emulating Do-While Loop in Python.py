# Emulating Do-While Loop in Python:

# do while loop just run the code at least once before riding into the loop condition.
# do while loop doesn't excist in the pyhton 
# still some mf aks question to imulate do while loop in python
# Yes, we can do this by an infinite while loop like this-
# while ture:
#     loop body;
    
while True:
    n = int(input("Enter a positve number: "))
    print(n)
    if (n<0):
        break
print("Break")