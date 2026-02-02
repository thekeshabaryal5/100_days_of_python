print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
with_out_tip = bill/people
# with_tip = (tip/100)*with_out_tip + with_out_tip
with_tip = with_out_tip*(1+tip/100)
print(round(with_tip,2))