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
          
5: Save the game
          
6: Load a save (DO THIS IF YOURE RELAUNCHING THE PROGRAM AND WANT TO KEEP YOUR PROGRESS)
          
7: Quit''') 
    gamechoice = input('') #spits the input prompt onto an empty new line so things look clean
    if gamechoice == '1':
        slots() #Placeholder function name for the game that will go here
        clear_screen()
    elif gamechoice == '2':
        blackjack() #Placeholder function name for the game that will go here
        clear_screen()
    elif gamechoice == '3':
        craps() #Placeholder function name for the game that will go here
        clear_screen()
    elif gamechoice == '4':
        roulette() #Placeholder function name for the game that will go here
        clear_screen()
    elif gamechoice == '5':
        savestate(balance, savecount)
        clear_screen()
    elif gamechoice == '6':
        loadsave()
        clear_screen()
    elif gamechoice == '7':
        quit()
    else:
        print('You have not input one of the options. Please try again.')
        main_menu()
        return


def loadsave():
    global balance
    global savecount
    print('This feature is under construction')
    with open('SaveState.txt', 'rb') as loadgame:
        valuestopull = pickle.load(loadgame)
        balance = int(valuestopull('Tokens'))
        savecount = int(valuestopull('SaveCount'))

def savestate(tokens, bootnum):
    with open('SaveState.txt', 'wb') as savegame:
        bootnum += 1
        objectstosave = {'Tokens':tokens, 'SaveCount':bootnum}
        pickle.dump(objectstosave, savegame)


def recordkeep():
    print('Under construction')

def clear_screen():
    #Git codespaces run on linux, so to make sure this works on both windows machines and codespaces i check to see what os the program is being run on and then call the clear command for that os 
    #Check the operating system name
    if os.name == 'nt':
        #Command for Windows
        _ = os.system('cls')
    else:
        #Command for Linux and macOS (posix)
        _ = os.system('clear')