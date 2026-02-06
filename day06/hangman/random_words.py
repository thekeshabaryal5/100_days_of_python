from wonderwords import RandomWord
import string
import re
import random

def get_random_word():
    random_word = RandomWord()
    lower_case_alphabet = string.ascii_lowercase
    while True:
        start_alphabet = random.choice(lower_case_alphabet)
        word = random_word.word(starts_with=start_alphabet,word_min_length=5,word_max_length=10)
        if re.fullmatch(r"[a-z]+",word):
            break
    
    return word