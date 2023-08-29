import random

print("Welcome to hangman")
print("-----------------------------------------------")

word_dict = ["aster" , "callalily" , "anemone" , "bellfower" , "camellia" , "colver" 
, "iris" , "jasmine" , "violet" , "rose"]

random_word = random.choice(word_dict)

for x in random_word:
    print("-" , end=" ")


def print_hangman(wrong):
    if wrong==0 :
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong==1:
        print("\n+---+")
        print("o   |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong==2:
        print("\n+---+")
        print("o    |")
        print("|    |")
        print("     |")
        print("   ===")
    elif wrong==3:
        print("\n+---+")
        print(" o   |")
        print("/|   |")
        print("     |")
        print("   ===")
    elif wrong==4:
        print("\n+---+")
        print(" o   |")
        print("/|\  |")
        print("     |")
        print("   ===")
    elif wrong==5:
        print("\n+---+")
        print(" o   |")
        print("/|\  |")
        print("/    |")
        print("   ===")
    elif wrong==6:
        print("\n+---+")
        print(" o   |")
        print("/|\  |")
        print("/ \  |")
        print("   ===")                


def print_word(guess_Letter):
    counter = 0
    rightLetters = 0
    for a in random_word:
        if (a in guess_Letter):
            print(random_word[counter] , end=" ") 
            rightLetters+=1
        else:
            print(" " , end=" ")
        counter+=1
    return rightLetters



def print_line():
    print("\r") 
    for a in random_word:
        print("\u203E") 


length_word = len(random_word)
amount_wrong = 0
current_guess_index = 0
current_letters_guess = []
current_letters_right = 0

while(amount_wrong != 6 and current_letters_right != length_word):
    print("\nLetter guessed so far")
    for letter in current_letters_guess : 
        print(letter , end=" ")
    LetterGuessed = input("\n guess a letter :")  
    # if input true
    if(random_word[current_guess_index]== LetterGuessed) :
        print_hangman(amount_wrong)

        current_guess_index+=1
        current_letters_guess.append(LetterGuessed)
        current_letters_right = print_word(current_letters_guess)
        print_line()
    else:
        amount_wrong+=1
        current_letters_guess.append(LetterGuessed
        )
        print_hangman(amount_wrong)

        current_letters_right = print_word(current_letters_guess)
        print_line()

    print("Game is over! Thank you for playing :)")    
