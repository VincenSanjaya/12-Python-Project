import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in words:
        word = random.choice(words)
        
    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        
        print('You have', lives, ' left and you haveused these character: ', ' '.join(used_letter))
        
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives = lives - 1
                print("Letter is not the word.")
                
        elif user_letter in used_letter:
            print("You have already used that character. Please try again")
        
        else:
            print("Invalid character. Please try again")
    
    if lives == 0:
        print("Sorry, you died. The word was", word)
    else :
        print("You guessed the word ", word, '!!')

    

hangman()