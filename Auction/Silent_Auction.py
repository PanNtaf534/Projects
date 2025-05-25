from Silent_Auction_Art import logo
print(logo)

bid_wars = {}
while True:
    name = input("What`s your name?")
    bidding = int(input("What`s your bid? $"))

    bid_wars[name] = bidding

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    if more_bidders == 'yes':
        print("\n" * 20)
    elif more_bidders == 'no':
        break
    else:
        print("Wrong input, please type 'yes' or 'no'.")

highest_bidder = max(bid_wars, key=bid_wars.get)
print(f"The winner is {highest_bidder} with a bid of ${bid_wars[highest_bidder]}!")
