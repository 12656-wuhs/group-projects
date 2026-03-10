import random

credits = 999999999999999999999999999999

def slots():
    global credits
    symbols = ['🍒','🍋','🍇','BAR','7']
    combo_current = []
    player_roll = []
    combo_select = 3
    player_RNG = 3
    print(f'Current Credits: {credits}')
    while True:
        while True:
            try:
                while True:
                    slots_bet = int(input('Place a bet: '))
                    if slots_bet > credits or slots_bet < 0:
                        print(f'You do not have {slots_bet}. Please enter a valid bet.')
                        continue
                    else:
                        break
            except ValueError:
                print('Please enter a valid bet.')
            break
        while combo_select > 3:
            select = random.choice(symbols)
            combo_current = combo_current + select
            combo_select = combo_select - 1
        while player_RNG > 3:
            select = random.choice(symbols)
            player_roll = player_roll + select
            player_RNG = player_RNG - 1
        if player_roll == combo_current:
            credits = credits + (slots_bet * 2)
            print('Jackpot!')
            while True:
                again = input('Would you like to play again? ').upper
                if again == 'Y':
                    continue
                elif again == 'N':
                    break
            break

slots()