# James Nickell  


# Period 6


# Craps


# Time Spent:


import random


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)




def craps():
    # Asks how many people
    player_count = int(input("How many players do you want in the game?: "))
    players = []
    for i in range(player_count):
        name = input(f"Enter the name of your player {i+1}: ")
        players.append({'name': name, 'balance': 1000})
    
    # Introduces the game of craps
    print(f"""------Welcome to craps------
        In the game of craps you roll 2 dice initially, this is called your 'come-out roll'
        This roll determines how high (or low) you have to roll for your next go. 
        However, there is a stipulation
        If you  roll a 7 or 11 you roll a 'natural'
        This results in an instant win
        There's also rolling a 2, 3, or 12.
        These result in an instant loss (craps)
        If you roll anything else, that will be your target number""")
        

    print("----Welcome to the craps table, you're going to lose all your balance MWAHHAHAHA----")    
    input("Press enter to roll the dice....")
    
    # The come-out roll
    total = roll_dice()
    print(f"You rolled a {total}")
    
    if total == 7 or total == 11:
        print("YOU WIN, it's a natural, and so are you")