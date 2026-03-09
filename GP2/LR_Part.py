import os
def main_menu():
    #Prints out a welcome message
    print(f'''Hello! Welcome to our humble casino, I hope you have a lovely time, and our options of games are as follows:
1: Slots
2: Blackjack
3: Craps
4: Roulette
5: Quit''')
    gamechoice = input('')
    if gamechoice == '1':
        slots() #Placeholder function name for the game that will go here
    elif gamechoice == '2':
        blackjack() #Placeholder function name for the game that will go here
    elif gamechoice == '3':
        craps() #Placeholder function name for the game that will go here
    elif gamechoice == '4':
        roulette() #Placeholder function name for the game that will go here
    elif gamechoice == '5':
        quit()
    else:
        print('You have not input one of the options. Please try again.')
        main_menu()
        return



def savestate():
    print('This function is still under construction.')