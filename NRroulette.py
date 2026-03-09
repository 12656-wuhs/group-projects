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
        print(f"/nYour current balance is {balance} chips!")
        
        #bet_amount is taking the amount of your 'balance' you are putting in
        bet_amount = int(input("Enter the amount you are betting: "))
        if bet_amount > balance:
            bet_amount = input("You don't got enough for that brokie do it again: ")
            continue

        #Choose what you are betting on. Either on one specific color, or on just the colors red or black.
        print("Choose what you would like to bet on: ")
        print("1 is a specific number (1-36) -- Payout is 35:1 ")
        print("2 is betting on either color (Red/Black) -- Payout 1:1")
        print("3 is betting on green (Green or zero) -- Payout is 38:1")
        choice = input("Please select 1, 2, or 3: ")
        

        #Defins the number of the spin
        winning_num = random.randint(0, 36)

        #Defines the colors of the wheel (Evens are red, odds are black, and zero is green.)
        if winning_num == 0:
            winning_color = 'Green'
        elif winning_num == % 2 == 0:
            winning_color = 'Red'
        else:
            winning_color = "Black"
