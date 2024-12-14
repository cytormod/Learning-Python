import os
from auction_logo import logo

print(logo)
print("Welcome to the Blind-Auction")

bids = {}

bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("what is your name?")
    price = int(input("Bid? $:"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Y' or 'N'." )
    if should_continue == "N":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "Y":
        os.system('clear')
