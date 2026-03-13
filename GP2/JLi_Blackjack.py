import random

# Constants
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

def create_deck():
    deck = [f"{rank} of {suit}" for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = sum(VALUES[card.split(' ')[0]] for card in hand)
    aces = sum(1 for card in hand if 'Ace' in card)
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def play_round(balance):
    print(f"Welcome to Blackjack!")
    print(f"In case you don't know to play Blackjack......")
    print(f"The goal of Blackjack is to beat the dealer by having a hand value closer to 21 than theirs without going over 21")
    print(f"when asked to hit, it means to get another card, and stand means to stay with your current card")
    print(f"For now, state how much money are you willing to risk.")
    print(f"Then the rest will follow as is.")
    print(f"Have fun gambling!")
    print(f"\n--- New Round --- Current Balance: ${balance}")
    
    # Place Bet
    while True:
        try:
            bet = int(input(f"Enter your bet (Max ${balance}): "))
            if 0 < bet <= balance:
                break
            print("Invalid amount.")
        except ValueError:
            print("Please enter a number.")

    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Player Turn
    while True:
        score = calculate_score(player_hand)
        print(f"The Dealer shows: {dealer_hand[0]} | Here's your hand: {player_hand} (Score: {score})")
        
        if score > 21:
            print("You Busted! ☠")
            return balance - bet
        
        move = input("Would you like to [H]it or [S]tand? ").lower()
        if move == 'h':
            player_hand.append(deck.pop())
        elif move == 's':
            break
        else:
            print(f" you suck, please enter h or s")

    # Dealer Turn
    print(f"Dealer reveals: {dealer_hand}")
    d_score = calculate_score(dealer_hand)
    while d_score < 17:
        dealer_hand.append(deck.pop())
        d_score = calculate_score(dealer_hand)
        print(f"Dealer hits: {dealer_hand} (Score: {d_score})")

    # Determine Winner
    p_score = calculate_score(player_hand)
    if d_score > 21 or p_score > d_score:
        print(f"You win! You are so good at this! 🎉 +${bet} 💰")
        return balance + bet
    elif p_score < d_score:
        print(f"Dealer wins...... you suck at this....😔 -${bet} 💸")
        return balance - bet
    else:
        print("Push (Tie). Bet returned. 😔")
        return balance

def main():
    balance = 500  # Starting chips
    while balance > 0:
        balance = play_round(balance)
        if balance <= 0:
            print("You're out of chips! ⛃⛂ Be better next time twin.")
            break
        if input("\n Wanna play another round? (y/n): ").lower() != 'y':
            break
    print(f"Final Balance: ${balance}. Thanks for playing! Gamble more of your life savings next time!")

if __name__ == "__main__":
    main()
