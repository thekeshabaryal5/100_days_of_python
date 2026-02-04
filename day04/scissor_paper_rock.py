from idlelib.sidebar import EndLineDelegator

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random 
human_choice = int(input('''What do you choose?
Type 0 for Rock,
1 for Paper, 
2 for Scissors.'''))

computer_choice = random.randint(0,2)
choice_to_picture = [rock,paper,scissors]
print(f'''{choice_to_picture[human_choice]}
Computer Choice:
{choice_to_picture[computer_choice]}
''')
if human_choice == computer_choice:
    print("It's a draw")
elif human_choice-computer_choice==1:
    print("You win")
else:
    print("You loose")