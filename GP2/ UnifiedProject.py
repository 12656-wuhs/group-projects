import random
import os
import pickle


import time

def roulette_game():
    balance = 1000
    print("Welcome to the Roulette table!")

    while balance > 0:
        print(f"\nYour current balance is {balance} chips!")
        

     #Choose what you are betting on. Either on one specific color, or on just the colors red or black.
        print("Choose what you would like to bet on: ")
        print("1 is a specific number (1-36) -- Payout is 35:1 ")
        print("2 is betting on either color (Red/Black) -- Payout 1:1")
        print("3 is betting on green (Green or zero) -- Payout is 38:1")
        print("4 is to stop playing here and leave with what ya got.")
        bet_type = input("Please select 1, 2, 3, or 4: ")

        if bet_type == '4':
            print("\n99 percent off gamblers quit before hitting big, bye")
            print(f"Final balance is {balance}")
            break

        #bet_amount is taking the amount of your 'balance' you are putting in
        bet_amount = int(input("Enter the amount you are betting: "))
        while bet_amount > balance:
            bet_amount = int(input("You don't got enough for that brokie do it again: "))
            continue

        if bet_type ==  '1':
            target = int(input("Pick a number (1-36): "))
            while target <1 or target > 36:
                target = int(input("That is not a correct option, please put a number 1-36: "))
            bet = 'number'
        
        elif bet_type == '2':
            target = input("Pick a color (red or black): ").lower()
            bet = "color"
        else:
            target = 0
            bet = 'Green'

        #Spins wheel cutely
        print("\nSpinning the wheel...............................................")
        time.sleep(1.5)
        
         #Defins the number of the spin
        winning_num = random.randint(0, 36)

        #Defines the colors of the wheel (Evens are red, odds are black, and zero is green.)
        if winning_num == 0:
            winning_color = 'Green'
        elif winning_num % 2 == 0:
            winning_color = 'Red'
        else:
            winning_color = "Black"

        print(f"---> The ball landed on {winning_num} ({winning_color.upper()} <---)")

        #Result logic
        win = False
        if bet == 'number' and target == winning_num:
            payout = bet_amount * 35
            win = True
            
        elif bet == 'color' and target == winning_color:
            payout = bet_amount
            win = True

        elif bet == 'Green' and target == winning_color:
            payout = bet_amount * 38
            win = True

        if win:
            balance += payout + bet_amount
            print(f"YAYAYAYAY WINNER!!!!!!! You won {payout} chips!")
        else:
            balance -= bet_amount
            print(f"Aw man, you lost {bet_amount} chips....")

    if balance <= 0:
        print("\nGame over, go home broke ***.")

if __name__ == '__main__':
    main_menu()
#end of nathaniels code

#beginnning of james's code
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)




def craps():
    # Establishes players
    player_count = int(input("How many players do you want in the game?: "))
    players = []
    for i in range(player_count):
        name = input(f"Enter the name of your player {i+1}: ")
        players.append({'name': name, 'balance': 1000})
        
    shooter_index = 0
    
    # Introduces the game of craps
    print("------Welcome to craps------")
    tutorial = input("If you'd like to know how the game works enter tutorial, if not, just press enter: ").lower()
    if tutorial == 'tutorial':
        print(f"""In the game of craps you roll 2 dice initially, this is called your 'come-out roll'
    This roll determines how high (or low) you have to roll for your next go. 
    However, there is a stipulation
    If you  roll a 7 or 11 you roll a 'natural'
    This results in an instant win
    There's also rolling a 2, 3, or 12.
    These result in an instant loss (craps)
    If you roll anything else, that will be your target number""")
        

    print("----Welcome to the craps table, you're going to lose all your balance MWAHHAHAHA----")    
    input("Press enter to roll the dice....")
    
    
    # Main Game Loop
    while True:
        shooter = players[shooter_index]
        print(f"\n--- This is a new round: {shooter['name']} is the shooter! ---")
        
        
        # Checks if the players have money
        active_players = [p for p in players if p['balance'] > 0]
        if not active_players:
            print("You're all out of money, sorry. Casino wins, baiiiii")
            break
    
        # Betting Phase
        current_bets = {}
        for p in active_players:
            print(f"{p['name']} Balance: ${p['balance']}")
            while True:
                try:
                    bet
    
    
        # The come-out roll
        point = roll_dice()
        print(f"You rolled a {point}")
        
        # These will decide what happens dependent on what you roll on your come out roll
        if point == 7 or point == 11:
            print("YOU WIN, it's a natural, and so are you")
        elif point == 2 or point == 3 or point == 12:
            print("You lose, you crapped out, you got it next time Queen or King")
        else:
            print(f"You didn't win or lose, you made it point which is {point}")
            
        # The Second Phase
        print("Alrighty roo, now that you have 'point' you get to roll again.\nYour goal is to hit point BEFORE rolling a 7.")
    
        while True:
            input("Press roll to enter again please...")
            pass_line = roll_dice()
            print(f"You rolled {pass_line}")
            
            
            if pass_line == 7:
                print("Well, you didn't get it this time. No worries tho, you'll get it next time.")
                break
            elif pass_line == point:
                print("You win, fantastic job. I'm proud of you")
                break
            else:
                print("Go ahead roll again.")
#End of James's code

#Beginning of my (Logans) code
savecount = None
balance = 1000
def main_menu():
    global savecount
    global balance
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
        slots_spin()
        clear_screen()
    elif gamechoice == '2':
        blackjack() #Placeholder function name for the game that will go here
        clear_screen()
    elif gamechoice == '3':
        craps()
        clear_screen()
    elif gamechoice == '4':
        roulette_game()
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


def recordkeep(gameresult, score):
    with open('Game Records.txt', 'w') as records:
        records.write(f'''Winner: {gameresult}
Score: {score}''')

def clear_screen():
    #Git codespaces run on linux, so to make sure this works on both windows machines and codespaces i check to see what os the program is being run on and then call the clear command for that os 
    if os.name == 'nt':
        #Command for Windows
        _ = os.system('cls')
    else:
        #Command for Linux and macOS (posix)
        _ = os.system('clear')
#end of my (Logan's) code

#Beginning of Nathaniels code
def roulette_game():
    global balance
    print("Welcome to the Roulette table!")

    while balance > 0:
        print(f"\nYour current balance is {balance} chips!")
        

     #Choose what you are betting on. Either on one specific color, or on just the colors red or black.
        print("Choose what you would like to bet on: ")
        print("1 is a specific number (1-36) -- Payout is 35:1 ")
        print("2 is betting on either color (Red/Black) -- Payout 1:1")
        print("3 is betting on green (Green or zero) -- Payout is 38:1")
        print("4 is to stop playing here and leave with what ya got.")
        bet_type = input("Please select 1, 2, 3, or 4: ")

        if bet_type == '4':
            print("\n99 percent off gamblers quit before hitting big, bye")
            print(f"Final balance is {balance}")
            break

        #bet_amount is taking the amount of your 'balance' you are putting in
        bet_amount = int(input("Enter the amount you are betting: "))
        while bet_amount > balance:
            bet_amount = int(input("You don't got enough for that brokie do it again: "))
            continue

        if bet_type ==  '1':
            target = int(input("Pick a number (1-36): "))
            while target <1 or target > 36:
                target = int(input("That is not a correct option, please put a number 1-36: "))
            bet = 'number'
        
        elif bet_type == '2':
            target = input("Pick a color (red or black): ").lower()
            bet = "color"
        else:
            target = 0
            bet = 'Green'

        #Spins wheel cutely
        print("\nSpinning the wheel...............................................")
        time.sleep(1.5)
        
         #Defins the number of the spin
        winning_num = random.randint(0, 36)

        #Defines the colors of the wheel (Evens are red, odds are black, and zero is green.)
        if winning_num == 0:
            winning_color = 'Green'
        elif winning_num % 2 == 0:
            winning_color = 'Red'
        else:
            winning_color = "Black"

        print(f"---> The ball landed on {winning_num} ({winning_color.upper()} <---)")

        #Result logic
        win = False
        if bet == 'number' and target == winning_num:
            payout = bet_amount * 35
            win = True
            
        elif bet == 'color' and target == winning_color:
            payout = bet_amount
            win = True

        elif bet == 'Green' and target == winning_color:
            payout = bet_amount * 38
            win = True

        if win:
            balance += payout + bet_amount
            print(f"YAYAYAYAY WINNER!!!!!!! You won {payout} chips!")
        else:
            balance -= bet_amount
            print(f"Aw man, you lost {bet_amount} chips....")

    if balance <= 0:
        print("\nGame over, go home broke ***.")

if __name__ == '__main__':
    main_menu()
#end of Nathaniels code

#beginning of James Lawsons code
def slots_spin(): #Rolls 3 random symbols
    symbols = ['🍒','🍋','🍇','BAR','7','🔔'] #slot machine symbols
    rows = [] #holds all 3 random symbols here
    for _ in range(3): #for loop for grabbing the 3 random symbols
        rows.append(random.choice(symbols)) #generates random symbol
    return rows #returns the rows list

def symbol_display(rows): #Displays what symbols the program rolled on
    print(f'''          ------- ------- -------
          |     | |     | |     |
          |     | |     | |     |
            {rows[0]}      {rows[1]}       {rows[2]}
          |     | |     | |     |
          |     | |     | |     |
          ------- ------- -------''')

def slots_valuer(rows,bet): #gives specific winning amount depending on symbols rolled
    global balance
    if rows[0] == rows[1] == rows[2]:
        if rows[0] == '🍒': #if all rows are cherries, doubles bet amount
            bet *= 2
            balance += bet
        elif rows[0] == 'BAR': #if all rows are BARs, triples bet amount
            bet *= 3
            balance += bet
        elif rows[0] == '🍋': #if all rows are lemons, quadruples bet amount
            bet *= 4
            balance += bet
        elif rows[0] == '🍇': #if all rows are grapes, quintuples bet amount
            bet *= 5
            balance += bet
        elif rows[0] == '🔔': #if all rows are bells, sextuples bet amount
            bet *= 6
            balance += bet
        elif rows[0] == '7': #if all rows are lucky 7's, septubples bet amount
            bet *= 7
            balance += bet
        print(f'Congrats! You won {bet}!')
    else:
        print('You won NOTHING! Better luck next time.')

def slots_game():
    global balance
    while True:
        try:
            bet = int(input("Place your bet: "))
            while True:
                if bet > balance or bet < 0:
                    print(f'You do not have {bet} in your balance. You have {balance} available.')
                    continue
                break
        except ValueError:
            print("Please enter a valid balance amount.")
            continue
        balance -= bet
        rows = slots_spin()
        symbol_display(rows)
        slots_valuer(rows,bet)
        print(f'Remaining Balance: {balance}')
        while True:
            replay = input('Would you like to replay [Y/N]? ').upper()
            if replay == 'Y':
                print('Starting new game...')
                break
            elif replay == 'N':
                print('Exiting game...')
                return
            else:
                print('Please enter a valid response.')
#End of James Lawsons code
main_menu()