import art
import flash_cards
import random

run_study_session = False
key_list = []
print(art.logo)
print("Shall we study? y or n:")
init = input()

if init == "y":
    run_study_session = True

while run_study_session:
    print("Good luck! Press esc anytime to quit!")
    print("===================================")
    # cycle through questions from flash_cards.study()
    # NEXT STEP: cycle questions at random by:
    # iterate through keys and save them in a list
    for key, value in flash_cards.cards.items():
        key_list.append(key)
    # perform an in-place shuffle of the keys
    random.shuffle(key_list)
    # loop through the list with a random index
    # use the random key to find its matching value in the library
    for key in key_list:
        print("Concept:")
        print()
        print(key)
        print()
        print("===================================")
        reveal = input("Show solution?")
        if reveal == 'y':
            print("===================================")
            print("Answer:")
            print()
            print(flash_cards.cards[key])
            print()
            print("===================================")
        if reveal == "esc":
                run_study_session = False
                print("==========================")
                print("Goodbye!")
                break

