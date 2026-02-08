# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

auction = {}
next_person = True
while next_person:
    name = input("Please enter your name: ")
    price = int(input("Please enter your price: $"))
    auction[name] = price
    have_next_person = input("Are there other person? yes/no: ").strip().lower()[0]
    if have_next_person != "y":
        next_person = False
    print("\n"*20)



max_amount = max(list(auction.values()))
name =list(filter(lambda x: x[1] == max_amount, auction.items()))[0][0]
print(f"Congratulations the winner is {name} with auction price of {max_amount}")