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

slots_game()