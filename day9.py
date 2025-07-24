from art import logo
print(logo)


# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


auction = {}


while True:
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))
    new = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    auction[name]=bid


    if new == "yes":
        print("\n"*150)
    if new == "no":
        break

for key, value in auction.items():
    print(f"Key: {key}, Value: {value}")

maximum= max(auction.values())

mname = [key for key, value in auction.items() if value == maximum]
print(auction)
print(mname)
print(f"The winner is {mname[0]} with a bid of ${maximum}")




