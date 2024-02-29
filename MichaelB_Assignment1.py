import random

def game(): # Defining the entire game as a function to make it easier to repeat
    print("Welcome to the game!")
    print("The rules are simple")
    print("I'm going to pick a number between 1-100, and you will have 3 guesses to pick the correct number")

    lives = 3   # Life counter
    winning_num = random.randint(1, 100)  # Generates the winning number randomly between 1 and 100

    print("The correct number is:", winning_num)  # Displays the winning number for testing purposes

    while lives > 0:  # This while loop allows the game to continue after failed guesses until the user loses all their lives
        guess = int(input("Make a guess: "))

        if guess == winning_num:
            print("Congratulations!!, you win!!")
            return lives  # As lives remaining and points awarded are directly connected, i return remaining lives as points for simplicity

        elif guess > winning_num:
            lives -= 1
            print("WRONG! Too high. Lives remaining:", lives)

        elif guess < winning_num:
            lives -= 1
            print("WRONG! Too low. Lives remaining:", lives)

    print("Game Over!! You Lose!!")
    return 0  # Return 0 points if the user loses

total_points = 0

while True:
    round_points = game() # Sets the round points to the return result of the the latest game
    total_points += round_points # Adds the points from the previous round to total points allowing score to be tracked across multiple rounds

    print(f"Total Points: {total_points}")

    rematch = input("Do you want to play again? (y/n): ").lower() # Following lines allow user to rematch without exiting the program
    if rematch != 'y':
        print("Thanks for playing! Your final total points: {total_points}. Goodbye.")
        break



