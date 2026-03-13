import random

balance = 999999999999999999999999999999

#Slots Game Functions

def slots_spin(): #Rolls 3 random symbols
    symbols = ['🍒','🍋','🍇','BAR','7','🔔'] #slot machine symbols
    rows = [] #holds all 3 random symbols here
    for _ in range(3): #for loop for grabbing the 3 random symbols
        rows.append(random.choice(symbols)) #generates random symbol
    return rows #returns the rows list

def symbol_display(rows): #Displays what symbols the program rolled on
    print(f'''____________________________________________
          
          ------- ------- -------
          |     | |     | |     |
          |     | |     | |     |
            {rows[0]}      {rows[1]}       {rows[2]}
          |     | |     | |     |
          |     | |     | |     |
          ------- ------- -------
          ''')

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

def slots_game(): #main function for the game
    global balance #makes balance a global variable
    while True: #with loop for replayability
        try: #tells the program to try this
            while True: #loops question if invald bet is made
                bet = int(input("Place your bet: ")) #user inputs bet here
                if bet > balance or bet < 0: #if bet invalid
                    print(f'You do not have {bet} in your balance. You have {balance} available.')
                    continue
                break
        except ValueError: #if user inputs anything other that integers
            print("Please enter a valid balance amount.")
            continue #loops if value error occurs
        balance -= bet #removes bet amount from balance
        rows = slots_spin() #makes the rows list equal to the symbols that are rolled in the slots_spin function, which is called
        symbol_display(rows) #calls symbol_display function and uses the rows list in the rows parameter
        slots_valuer(rows,bet) #calls slots_valuer function and uses the rows list and bet variable in the rows and bet parameter
        print(f'''____________________________________________
              
Remaining Balance: {balance}
____________________________________________
''') #prints current balance after win/lose is shown

        while True: #loops incase of invalid response
            replay = input('Would you like to replay [Y/N]? ').upper() #Asks if player wants to replay
            if replay == 'Y': #if the player wants to replay, it breaks this loop, leading to the game looping
                print('''
                      
                      Starting new game...

                      ''')
                break #breaks this loop, loops the main loop
            elif replay == 'N': #if the player wants to quit, returns function, leading function to end
                print('''
                      
                      Exiting game...

                      ''')
                return
            else: #if player enters invalid response
                print('Please enter a valid response.')

slots_game()