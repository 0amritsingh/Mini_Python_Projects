# Rock Paper Seassios game [version 1.0]
import random
    
def gamesystem():
    items = ["ROCK🗻", "PAPER📜", "SCISSORS ✂"]
    
    print("\nChoose your Move:")  
    print("1. ROCK🗻\n2. PAPER📜\n3. SCISSORS ✂")
    
    # User Input:
    umove = int(input("\n>>> "))
    
    if (umove == 1):
        print("\nYou:", items[0] )
    elif (umove == 2):
        print("\nYou:", items[1] )
    elif (umove == 3):
        print("\nYou:", items[2] )
    else:
        print("Invailed input. Try again!")
        
    # Python Input:
    pymove = random.randrange(1, 4) # this line of code defines that the playing bot will take random moves like totaly random as we imported random module
    
    if (pymove == 1):
        print("Python:", items[0] )
    elif (pymove == 2):
        print("Python:", items[1] )
    elif (pymove == 3):
        print("Python:", items[2] )
    else:
        print("Invailed input. Try again!")
        
    # Win or Loose Situation:
    if   (umove == 1 and pymove == 1):
        print("\nDraw!\n")
    elif (umove == 1 and pymove == 2):
        print("\nYou Loose!\n")
    elif (umove == 1 and pymove == 3):
        print("\nYou Win!\n")
        
    elif (umove == 2 and pymove == 1):
        print("\nYou Win!\n")
    elif (umove == 2 and pymove == 2):
        print("\nDraw!\n")
    elif (umove == 2 and pymove == 3):
        print("\nYou Loose!\n")
        
    elif (umove == 3 and pymove == 1):
        print("\nYou Loose!\n")
    elif (umove == 3 and pymove == 2):
        print("\nYou Win!\n")
    elif (umove == 3 and pymove == 3):
        print("\nDraw!\n")
    
    again = int(input("Wanna Play again?\n1. Yes     2. No \n>>> "))
    if (again == 1):
        print("____________________")
        gamesystem()
    elif (again == 2):
        print("\nThanks! for playing. Come Again!\n")
        quit()

gamesystem()
