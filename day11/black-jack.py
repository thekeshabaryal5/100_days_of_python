import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_game_on = True
is_playing = True
safe_to_play = True
user_won = False


computers_card = []
player_cards = []
for _ in range(2):
    computers_card.append(random.choice(cards))
    player_cards.append(random.choice(cards))

print(f"Computer have first card: {computers_card[0]}")
print(f"You have: {player_cards}")


while safe_to_play and is_playing:
    decision = input("Do you want to add more card (y/n): ").lower().strip()[0]
    if decision == "y":
        player_cards.append(random.choice(cards))
        print(f"You have: {player_cards}")
        safe_to_play = True if sum(player_cards)<22 else False
    else:
        is_playing = False
        
user_won = safe_to_play
while safe_to_play and (sum(computers_card)<22):
    if sum(computers_card) > sum(player_cards):
        user_won = False
        break
    else:
        print("Adding cards...")
        computers_card.append(random.choice(cards))
        print(f"Computers card: {computers_card}")
        
    
if user_won:
    print(f"You won")
else:
    print("You lost")