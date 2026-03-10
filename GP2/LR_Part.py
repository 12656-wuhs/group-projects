import os
import pickle
savecount = None
balance = 100
def main_menu():
    #Prints out a welcome message
    print(f'''Hello! Welcome to our humble casino, I hope you have a lovely time, and our options of games are as follows:
1: Slots
2: Blackjack
3: Craps
4: Roulette
5: Quit''') 
    gamechoice = input('') #spits the input prompt onto an empty new line so things look clean
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


def loadsave(tokens, bootnum):
    global balance
    
    with open('SaveState.txt', 'r') as loadgame:
        loadgame.readlines
        for line in loadgame:
            if 'Tokens:' in line:
                line.strip('Tokens:')
                tokens = int(line)
            if 'Save Count: ' in line:
                line.strip('Save Count: ')
                bootnum = int(line)
    print('This feature is under construction')

def savestate(tokens, bootnum):
    with open('SaveState.txt', 'w') as savegame:
        objectstosave = {'Tokens':tokens, 'SaveCount':bootnum}


def recordkeep():
    print('Under construction')