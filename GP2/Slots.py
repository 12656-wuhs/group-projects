import random

balance = 999999999999999999999999999999

#Slots Game Functions

def slots_spin():
    symbols = ['🍒','🍋','🍇','BAR','7','🔔']
    
    return [random.choice(symbols) for _ in range(3)]

def symbol_display(rows):
    print(f'''------- ------- -------
          |     | |     | |     |
          |     | |     | |     |
        {rows[0]} {rows[1]} {rows[2]}
          |     | |     | |     |
          |     | |     | |     |
          ------- ------- -------''')

def slots_valuer(rows,bet):
    global balance
    if rows[0] == rows[1] == rows[2]:
        if rows[0] == '🍒':
            bet *= 1
            balance += bet
        elif rows[0] == '🍋':
            bet *= 1
            balance += bet
        elif rows[0] == '🍇':
            bet *= 1
            balance += bet
        elif rows[0] == '🍒':
            bet *= 1
            balance += bet
        elif rows[0] == '🍒':
            bet *= 1
            balance += bet

def slots_game(bet):
    global balance
    while True:
        try:
            bet = int(input("Place your bet: "))
            while True:
                if bet > balance or bet < 0:
                    print(f'You do not have {bet} in your balance. Please enter a valid bet.')
                    continue
                break
        except ValueError:
            print("Please enter a valid balance amount.")
            continue
        slots_spin()
        symbol_display()
        slots_valuer()
        slot_replay()
        
def slot_replay():
    while replay == 'Y':
        replay = input('Would you like to replay? ').upper
        if replay == 'Y':
            print('Starting new game...')
            slots_game()
        elif replay == 'N':
            print('Exiting game...')

        else:
            print('Please enter a valid response.')
            continue

slots_game(bet = 0)