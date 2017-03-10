import random
from time import *

def print_debug():
    print("wow, debug stats: ")
    print("Guesses: ", Guesses)
    print("Number: ", Number)
    print("DifficultySelect: ", DifficultySelect)
    print("That's all the variables. Debugging complete!")

def random_tip():
    tip = random.randrange(1,11)
    if DifficultySelect.lower() == "insane":
        print("***pro-tip: you should not have picked this mode.***")
    else:
        if tip == 1:
            print("***pro-tip: typing any words or letters will take off 1 guess and will always be wrong... only type numbers if you wish to succeed!***")
            print("~~~~~")
        elif tip == 2:
            print("***pro-tip: if you selected easy mode, your number will always be between one and fifty.***")
            print("~~~~~")
        elif tip == 3:
            print("***pro-tip: if you selected medium mode, your number will always be between one and one hundred.***")
            print("~~~~~")
        elif tip == 4:
            print("***pro-tip: if you selected hard mode, your number will always be between one and two hundred-fifty.***")
            print("~~~~~")
        elif tip == 5:
            print("***pro-tip: always use your guesses wisely, you are only given a few of 'em***")
            print("~~~~~")
        elif tip == 6:
            print("***pro-tip: if you selected easy mode, you will start your game with thirteen guesses. Use them wisely***")
            print("~~~~~")
        elif tip == 7:
            print("***pro-tip: if you selected medium mode, you will start your game with nine guesses. Use them wisely***")
            print("~~~~~")
        elif tip == 8:
            print("***pro-tip: if you selected hard mode, you will start your game with only five guesses! Use them wisely***")
            print("~~~~~")
        elif tip == 9:
            print("***pro-tip: apparently you have to convert strings to integers before comparing them in python. pssh... my computer's smart enough to know what letters mean!***")
            print("~~~~~")
        elif tip == 10:
            print("***pro-tip: if you are within three of the correct answer, the program will tell you that you are super close, BUT not if you are too high or too low!***")
            print("~~~~~")
        elif tip == 11:
            print("***pro-tip: if the python console is getting a bit messy from all of this text, click the icon in the top left corner, select properties and pick a nicer color, you deserve it :)***")
            print("~~~~~")

Tries = 0
Guesses = 0
Number = 0

print("Hello and welcome to \"guess the number\"!")
while True:
    DifficultySelect = input("Select a difficulty: easy, medium or hard ~ ")
    if DifficultySelect.lower() == "easy" or DifficultySelect.lower() == "e":
        #Code to run, if the user enters 'easy' in response to the difficulty level.
        print("~~~~~")
        print("You chose easy mode! Hey, I won't judge, not everybody is as good as I am at guessing numbers. Have fun!")
        print("~~~~~")
        Guesses = 13
        Number = random.randrange(1, 50)
        break
    elif DifficultySelect.lower() == "medium" or DifficultySelect.lower() == "m":
        #Code to run, if the user chooses the 'medium' difficulty level.
        print("~~~~~")
        print("You chose normal mode! As the name implies, this mode is truely the most average of the modes, not too hard, not too easy. It's a good way to see if you are good at guessing randomlly generated numbers.")
        print("~~~~~")
        Guesses = 9
        Number = random.randrange(1, 100)
        break
    elif DifficultySelect.lower() == "hard" or DifficultySelect.lower() == "h":
        #Code to run if the user enters hard as the difficulty level.
        print("~~~~~")
        print("You chose hard mode! This mode is no joke. The number will be randomly generated from one to two hundred and fifty! You get three tries, make them count. Good luck.")
        print("~~~~~")
        Guesses = 5
        Number = random.randrange(1, 250)
        break
    elif DifficultySelect.lower() == "insane":
        print("~~~~~")
        print("Who told you about this mode?! Was it me? it was probably me. Have fun with your 3 guesses. You better be pretty lucky...")
        print("~~~~~")
        Guesses = 3
        Number = random.randrange(1, 500)
        break
    elif DifficultySelect.lower() == "debug":
        print("~~~~~")
        print("The game hasn't even started and you already want to see debugging stuff? Well ok, I guess: ")
        print("~~~~~")
        print_debug()
    else:
        print("~~~~~")
        print("Sorry, I don't know how to respond to that, for I am but a humble machine *beep* *boop*")
        print("~~~~~")
while True:
    if Guesses > 0:
        UserGuess = input("     Have a guess! ~ ")
        if UserGuess.lower() == "debug":
            print_debug()
        else:
            Tries = Tries + 1
            Guesses = Guesses - 1
            print("~~~~~")
            print("You guessed", UserGuess)
            print("~~~~~")
            if int(UserGuess) < (Number - 3):
                print("Sorry,", UserGuess, "is too low... You now have", Guesses, "guesses left.")
                print("~~~~~")
                random_tip()
            elif int(UserGuess) > (Number + 3):
                print("Sorry,", UserGuess, "is too high... You now have", Guesses, "guesses left.")
                print("~~~~~")
                random_tip()
            elif (int(UserGuess) - Number > -4 and int(UserGuess) - Number < 4) and int(UserGuess) != Number:
                print("You're close!! You now have", Guesses, "guesses left.")
                print("~~~~~")
                random_tip()
            else:
                print("Congrats! You won!! I hope you had fun! Please play again sometime!")
                sleep(3)
                print("Self-destructing in 3")
                sleep(2)
                print("2")
                sleep(1)
                print("1")
                sleep(0.5)
                break

    else:
        print("Oh no! You're out of guesses! You lose. :(")
        sleep(1)
        print("Self-destructing in 3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(0.5)
        break
