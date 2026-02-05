import string
import random
import pyperclip
print("Welcome to the monsterPassword generator")
upper_case_letters = [chr(x) for x in range(ord('A'),ord('A')+26)]
lower_case_letters = [chr(x) for x in range(ord('a'),ord('a')+26)]
letters = upper_case_letters+lower_case_letters
random.shuffle(letters)
numbers = [x for x in range(10)]
random.shuffle(numbers)
symbols = list(string.punctuation)
random.shuffle(symbols)

number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like? "))
number_of_numbers = int(input("How many numbers would you like? "))

password =[]
for x in range(number_of_letters):
    password.append(random.choice(letters))
for x in range(number_of_symbols):
    password.append(random.choice(symbols))
for x in range(number_of_numbers):
    password.append(str(random.choice(numbers)))
    
random.shuffle(password)
password = "".join(password)
pyperclip.copy(password)
print(password)
print("Your password is copied to your clipboard.")