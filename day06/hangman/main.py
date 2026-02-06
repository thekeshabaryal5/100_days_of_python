import random_words
import life_stage


word = random_words.get_random_word()
display_word = ["_ "for x in word]
is_game_on = True
life_stages = life_stage.stages
life = len(life_stage.stages)-1
guessed_history = []


# start of the program
print("Welcome to hangman")
while is_game_on:
    print(f"Word to guess: {"".join(display_word)}")
    print(f"Previously guessed: {guessed_history}")
    guessed_word = input("Guess a letter: ").strip().lower()[0]
    
    while guessed_word in guessed_history:
        guessed_word= input(f"You already guessed {guessed_word}.Guess a new word:  ").strip().lower()[0]
        
    guessed_history.append(guessed_word)
    occurrence = word.count(guessed_word)
    start_index = 0
    # print(occurrence)
    if occurrence:
        while occurrence:
            index = word.find(guessed_word,start_index)
            start_index = index+1
            display_word[index]=guessed_word
            occurrence -= 1
            is_game_on = display_word.count("_ ")>0
    else:
        life -= 1
        print(f"You guessed {guessed_word}, that's not in the word. You lose a life")
        is_game_on = life>0
        
    print(life_stages[life])
    print(f"********************{life}/{len(life_stages)-1} LIVE LEFT**************")
    
if life>0:
    print(f"Congratulations!!! you guessed it correct- {word}")
else:
    print(f"Oh no! You lost. The word was {word}")
    
print("GAME OVER")