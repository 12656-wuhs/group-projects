#Nathaniel Rodriguez
#Period 6
#Roulette for hackathon
#Time spent: 

import random
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
            print("99 percent off gamblers quit before hitting big, bye")
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
            balance += payout
            print(f"YAYAYAYAY WINNER!!!!!!! You won {payout} chips!")
        else:
            balance -= bet_amount
            print(f"Aw man, you lost {bet_amount} chips....")

    if balance <= 0:
        print("\nGame over, go home broke ***.")

if __name__ == '__main__':
    roulette_game()