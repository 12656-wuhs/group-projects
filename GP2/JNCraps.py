# James Nickell  


# Period 6


# Craps


# Time Spent:


import random


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
        
        
        
        
craps()