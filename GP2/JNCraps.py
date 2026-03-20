# James Nickell  


# Period 6


# Craps


# Time Spent:


import random



def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)




def craps():
    starting_balance = 1000
    # Establishes players
    try:
        player_count = int(input("How many players do you want in the game?: "))
    except ValueError:
        print("Defaulting to 1")
        player_count = 1
       
    players = []
    for i in range(player_count):
        name = input(f"Enter the name of your player {i+1}: ")
        players.append({'name': name, 'balance': starting_balance})
        
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
        


    
    
    # Main Game Loop
    while True:
        
        # Checks if players have money
        active_players = [p for p in players if p['balance'] > 0]
        if not active_players:
            print("You're all out of money, sorry. Casino wins, baiiiii")
            break
        
        
        shooter = active_players[shooter_index % len(active_players)]
        print(f"\n--- This is a new round: {shooter['name']} is the shooter! ---")
        
    
        # Betting Phase
        current_bets = {}
        for p in active_players:
            print(f"{p['name']} Balance: ${p['balance']}")
            while True:
                try:
                    print(f"\n{p['name']} Balance: ${p['balance']}")
                    bet = int(input("Place your bets: $"))
                    if 0 < bet <= p['balance']:
                        current_bets[p['name']] = bet
                        break
                    else:
                        print("Invalid amount. Must be between $1 and ${p['balance']}")
                except ValueError:
                    print("Please enter an actual number ♥")
    
        # The come-out roll
        print("----Welcome to the craps table, you're going to lose all your balance MWAHHAHAHA----")    
        input("Press enter to roll the dice....")
        point = roll_dice()
        print(f"You rolled a {point}")
        
        round_result = None
        
        # These will decide what happens dependent on what you roll on your come out roll
        if point == 7 or point == 11:
            print("YOU WIN, it's a natural, and so are you")
            recordkeep("Craps", 'Win', point)
            round_result = 'win'
        elif point == 2 or point == 3 or point == 12:
            print("You lose, you crapped out, you got it next time Queen or King")
            recordkeep('Craps', 'Loss', point)
            round_result = 'lose'
            shooter_index += 1
        else:
            print(f"You didn't win or lose, you made it point which is {point}")
            round_result = 'none'
            
        # The Second Phase
        
        if round_result == 'none':
            print("Alrighty roo, now that you have 'point' you get to roll again.\nYour goal is to hit point BEFORE rolling a 7.")
            while True:
                input("Press roll to enter again please...")
                pass_line = roll_dice()
                print(f"You rolled {pass_line}")
                
                
                if pass_line == 7:
                    print("Well, you didn't get it this time. No worries tho, you'll get it next time.")
                    round_result = 'lose'
                    shooter_index += 1
                    recordkeep('Craps', 'Loss', pass_line)
                    print('Would you like to continue? (y/n)')
                    donecheck = input(' ')
                    if donecheck == 'y':
                        craps()
                        return
                    break
                elif pass_line == point:
                    print("You win, fantastic job. I'm proud of you")
                    recordkeep('Craps', 'Win', pass_line)
                    round_result = 'win'
                    print('Would you like to continue? (y/n)')
                    donecheck = input(' ')
                    if donecheck == 'y':
                        craps()
                        return
                else:
                    print("Go ahead roll again.")
                    
                    
                # Payout 
            for p in active_players:
                bet = current_bets[p['name']]
                if round_result == 'win':
                    p['balance'] += bet
                else:
                    p['balance'] -= bet
                print(f"{p['name']} now has ${p['balance']}")
         
        # Asks if you wanna play again   
        if input("\nPlay another round? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break
        
        
        
        
craps()