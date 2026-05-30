import random

def main():

    while True:
        print("--- Blackkack ---")
        print("1. Play")
        print("2. Exit")

        choice = int(input("Enter a number to choose: "))

        if choice == 1:
            deck = create_deck()
            player_hand = []
            dealer_hand = []

            player_hand.append(deal_card(deck))
            player_hand.append(deal_card(deck))

            dealer_hand.append(deal_card(deck))
            dealer_hand.append(deal_card(deck))

            print("\nYour hand:", player_hand, "Total:", calculate_total(player_hand))
            print("Dealer shows:", dealer_hand[0])

            player_total = player_turn(deck, player_hand)

            if player_total > 21:
                print("You bust!")
                continue


            dealer_total = dealer_turn(deck, dealer_hand)

            result = determine_winner(player_total, dealer_total)
            print(result)

        elif choice == 2:
            print("Goodbye!")
            break

        else:
            print("Enter a number please.")


def create_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [rank for rank in ranks for _ in range(4)]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop()
    
    
def calculate_total(hand):
    value_map = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
          "J": 10, "Q": 10, "K": 10, "A": 11
    }

    total = sum(value_map[c] for c in hand)
    aces = hand.count("A")

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total

def player_turn(deck, player_hand):
    while True:
        total = calculate_total(player_hand)
        print("\nYour hand:", player_hand, "Total:", total)

        choice = input("Hit or Stand: ").lower()

        if choice == "hit":
            player_hand.append(deal_card(deck))
            total = calculate_total(player_hand)
            print("You drew: ", player_hand[-1])

            if total > 21:
                return total
            
        elif choice == "stand":
            return total
        
        else:
            print("You can only enter Hit or Stand.")
            
def dealer_turn(deck, dealer_hand):
    print("\nDealer reveals:", dealer_hand, "Total:", calculate_total(dealer_hand))
   
    while True:
        total = calculate_total(dealer_hand)

        if total < 17:
            dealer_hand.append(deal_card(deck))
            print("Dealer drew: ", dealer_hand[-1])
        
        elif total > 21:
            print("Dealer busts with:", total)
            return total

        else:
            print("Dealer stands with: ", total)
            return total


def determine_winner(player_total, dealer_total):
    if dealer_total > 21:
        result = "Dealer Bust. Player wins!"
        return result
   
    if player_total > 21:
        result = "Player Bust. Dealer wins!"
        return result
    
    if player_total < dealer_total:
        result = "Dealer wins!"
        return result
    
    elif player_total > dealer_total:
        result = "Player wins!"
        return result
    
    else:
        result = "Push (tie)"
        return result

main()