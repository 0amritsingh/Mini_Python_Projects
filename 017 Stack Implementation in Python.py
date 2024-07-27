# Stack Implementation in Python [version: 0.1] 

print('Stack Operations in Python')
stack = []

def push():
    item = input('\nEnter Item: ')
    stack.append(int(item)) if item.isnumeric() == True else stack.append(item)
    print('Pushed Successfully!')
    more = input('Push more? (y/n): ')
    push() if more in 'yY' else None
def pop():
    print('\nStack is Empty!') if len(stack) == 0 else print(f'\n{stack.pop()} - Popped Successfully!')
    more = input('Pop more? (y/n): ')
    pop() if more in 'yY' else None
def peek():
    print('\nStack is Empty!') if len(stack) == 0 else print(f'Peeked Item: {stack[-1]}')
    more = input('Peek more? (y/n): ')
    peek() if more in 'yY' else None
while True:
    user = input('\n++++++++++++++++++++\nPress [1]: Push\nPress [2]: Pop\nPress [3]: Peek\nPress [4]: Display\nPress [5]: Exit\n~> ')
    push() if user == '1' else pop() if user == '2' else peek() if user == '3' else print(f'\nStack: {stack}') if user == '4' else exit() if user == '5' else print('\nERROR 101: Wrong input!')

# online study matrial(theory/concept) of Stack: https://www.geeksforgeeks.org/stack-in-python
 