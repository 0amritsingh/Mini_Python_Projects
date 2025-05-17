# Kirana Store Ration Calculator [version: 0.1] 

amount = 0
print('Calulate your total bill or Q to quit\n')
while True:
    user_input = input('Enter amount: ')
    if user_input in 'Qq':
        print(f'Your total bill is {amount}')
        break
    else:
        amount = amount + int(user_input)
        print(f'Your total amount is {amount} so far\n')

# I next version we'll create proper kirana recipt by adding item name and qty, etc.