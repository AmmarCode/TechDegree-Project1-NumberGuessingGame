import random
high_score = None


def start_game(high_score):
    print("-------------------------------------")
    print("Welcome to the Number Guessing Game! ")
    print("-------------------------------------")
    while True:
        print(f"Current high score is {high_score}")
        random_num = random.randint(1, 10)
        guess = 0
        count = 0
        # Kick off the program by calling the start_game function.
        # Continuously prompt the player for a guess.
        while guess != random_num:

            try:
                guess = input("Pick a number between 1 and 10:  ")
                guess = int(guess)
            except ValueError:
                print("Oops! Invalid entry, Please pick a number between 1 and 10, Enter the number in (Digit) form")
                continue
            if guess > 10 or guess < 1:
                print("Oops! Your number is out of range, Please pick a number between 1 and 10 ")
                continue

            count += 1
            # If the guess greater than the solution, display to the player "It's lower".
            if guess > random_num:
                print("It's lower")
            # If the guess is less than the solution, display to the player "It's higher".
            elif guess < random_num:
                print("It's higher")
            elif guess == random_num:
                print(f"you guessed it in {count}attempts")
                if high_score is None or high_score > count:
                    high_score = count
                    if high_score == 1:
                        print(f"$$$ Congratulations! You got it in 1 attempt $$$")
                    else:
                        print(f"Great! you set a new record {high_score} attempts")
        if high_score == 1:
            print(f"Your highest score is 1 attempt")
        else:
            print(f"Your highest score is {high_score} attempts")
        play_again = input("Would you like to play again? [Y]es or [N]o  ")
        if play_again.lower() != "y":
            print("**** Closing Game, See you next time! ****")
            break


start_game(high_score)
