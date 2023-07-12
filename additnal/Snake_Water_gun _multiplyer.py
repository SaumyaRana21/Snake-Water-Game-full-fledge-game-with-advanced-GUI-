import random 
print("WELCOME TO THE GAME:- ")
player1=input("USER 1:\n OPTIONS: Choose S for Snake \n Choose W for Water \n Choose G for Gun \n Your option: ")
print("\n")
player2=input('''USER 1:\n OPTIONS: Choose S for Snake \n Choose W for Water \n Choose G for Gun \n Your option: ''')
print()

print("player 1 choose: ",player1 , "\n player 2 choose: ",player2)
def gamewin(player1_choice,player2_choice):
    if player1 == player2:
        print("IT'S A TIE!")
    elif player1 == 'W':
        if player2 == 'S':
            return True
        elif player2 == 'G':
            return False
    elif player1 == 'G':
        if player2 == 'S':
            return False
        elif player2 == 'W':
            return True
    elif player1 == 'S':
        if player2 == 'W':
            return False
        elif player2 == 'G':
            return True

player1_choice = 'G'
player2_choice = 'S'
result = gamewin(player1_choice, player2_choice)

if result == True:
    print("PLAYER 2 WON!")
elif result == False:
    print("PLAYER 1 WON!")
else:
    print(result)

   