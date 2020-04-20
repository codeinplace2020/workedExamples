import random

MIN_NUMBER = 1
MAX_NUMBER = 100

def main():
    print("Hello! Let's play a number guessing game.")
    print("Press ctrl-c to quit.")

    # Collect the user's name to make the game more personal
    user_name = input("Please enter your name: ")

    while True:
        # pick a random integer in the interval [MIN_NUMBER, MAX_NUMBER]
        target = random.randint(MIN_NUMBER, MAX_NUMBER)

        # initialize a variable for the user's guess
        user_guess = 0

        print(
            user_name + ", I'm thinking of an integer in the interval ["
            + str(MIN_NUMBER) + ", " + str(MAX_NUMBER) + "]")
        
        # Run the current game until the user guesses the correct value
        while user_guess != target:
            user_guess = int(input("Please enter your guess: "))

            # Handle guesses outside of allowable range and provide feedback
            # to the user so they can refine their guess.
            if user_guess > MAX_NUMBER or user_guess < MIN_NUMBER:
                print(user_name + ", your guess was out of range!")
            elif user_guess < target:
                print(user_name + ", your guess was too low!")
            elif user_guess > target:
                print(user_name + ", your guess was too high!")
            else:
                print("Congratulations " + user_name + ", you got it!")
            
            print("")

if __name__ == "__main__":
    main()
