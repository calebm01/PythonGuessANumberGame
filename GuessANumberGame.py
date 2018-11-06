# Project 4
# Caleb Mouritsen, Colton Horthcutt
#
# Program that allows the user to guess a number between 1 and 100, there's also an option to gamble on the outcome if the user
# wants

#importing random to allow the program to get random numbers for the user to guess
import random



#Function that runs if the user wants to play the flip a coin game
def flip_a_coin():
    #randomizing the coin toss
    coin = ["Heads", "Tails"]
    side = random.choice(coin)

    #While loop prompting the user to guess what the coin will land on
    while True:
        guess = input("Will the coin land head or tails? ").title()
        if guess == "Heads" or guess == "Tails":
            break
        #Make sure the users is inputting the correct things
        else:
            print("enter heads or tails")

    #If statements determining whether the user's guess was correct or not
    if guess == side:
        print("You guessed correctly")
        print("You win!")
        menu()
    elif guess != side:
        print("You guessed wrong")
        print("you lose")
        menu()


#play function runs if the user decides to play the guessing game    
def play():
    print("Welcome to the guessing game!")
    #while loop, allows the user to input the first integer in the guessing range. Cast to int
    while True:
        range = input("What is the first number in the range you want to guess from?")
        if range.isdigit():
            range = int(range)
            break
        #make sure the input is a number
        else:
            print("Input needs to be a number")

    #Second while loop to determine the final number in the guessing range. Cast to int
    while True:
        range2 = input("What is the last number in the range you want to guess from?")
        if range2.isdigit():
            range2 = int(range2)
            break

    
        #Make sure the input is a number
        else:
            print("Input needs to be a number")
            
    if range > range2:
        temp = range
        range = range2
        range2 = temp

    #While loop for number of chances the user wants. Cast to int
    while True:
        chances = input("How many chances to guess do you want?")
        if chances.isdigit():
            chances = int(chances)
            break
        #make sure the input is a number
        else:
            print("Input needs to be a number")


    #Initialize the random number between the range chosen, tell the user what they need to do to win the game
    number = random.randint(range,range2)
    print("You're trying to guess a number between", range, "and", range2)
    print("You have", chances, "guesses")
    guess_count = 0

    #While loop to make sure the user gets the correct amount of guesses that they chose
    while guess_count < chances:
        #While loop asking the user what the number is, makes sure the guess is a number and is within the range
        #that the user chose
        while True:
            guess = input("What is the number between " + str(range) + " and " + str(range2))
            if guess.isdigit() and int(guess) < range2 and int(guess) > range:
                guess = int(guess)
                break
            else:
                print("Guess need to be a number between", range, "and", range2)

        #If statements letting the user know if they need to guess higher or guess lower
        if guess < number:
            print("You need to guess a higher number")
            guess_count += 1
        elif guess > number:
            print("You need to guess a lower number")
            guess_count += 1
            
        #User wins
        elif guess == number:
            print("You guessed the number in", guess_count, "guesses")
            print("You win!")
            menu()
        
    #User doesn't guess the correct number       
    print("You didn't guess the number in the given number of tries :(")
    print("The number was", number)
    menu()
    
#credits function, shows user who made the game
def credits():
    print("Game made by Caleb Mouritsen and Colton Northcutt \n Thanks for playing!")
    menu()
    
#quit function runs if the user decides to quit in the menu
def quit():
    print("Thanks for playing!")

    
#Function that contains the menu, first thing the user will see
def menu():
    #Greeting and options
    print("Welcome to the guessing game!")
    
    #User input to choose what they want to do
    userchoice = input("\n Enter p to play the guessing game, enter f to play the flip a coin game, enter c to view the credits, or enter q to exit the game")

    #If statement checking what the input was, program will send user to different functions depending on their choice.
    if userchoice == "p":
        play()

    elif userchoice == "c":
        credits()

    elif userchoice == "q":
        quit()

    elif userchoice == "f":
        flip_a_coin()
    else:
        print("Please enter a valid input")
        menu()

menu()
