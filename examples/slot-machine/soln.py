import random
import time

STARTING_BALANCE = 10
SPIN_COST = 1
SPIN_PAUSE_INTERVAL = 0.5
WINNINGS_FOR_TWO = 10
WINNINGS_FOR_THREE = 100


def main():
    print("""
    Welcome to the Python Slot Machine. You have been allotted 100 tokens to
    begin. To see your balance type "b". To spin the machine type "s". 
    Additional help can be found by typing "h". Good luck!
    """)

    balance = STARTING_BALANCE

    while True:
        cmd = normalize_cmd(input("> "))

        if cmd == "balance":
            print("Your current balance is: " + str(balance))
        elif cmd == "spin":
            winnings = spin()

            if winnings <= 0:
                print("Better luck next time!")
            else:
                print("You just won " + str(winnings) + " tokens!")

            balance += winnings
        elif cmd == "help":
            show_help()
        elif cmd == "exit":
            print("Thanks for playing.\n")
            exit(0)
        else:
            print("Unrecognized command. Type 'help' for available commands.")


        if balance <= 0:
            print("You ran out of tokens. Game over!")
            return


def normalize_cmd(cmd):
    """
    This function converts shorthand commands to their full counterparts. It
    also removes extraneous capitalization and spacing.
    """
    cmd = cmd.strip().lower()

    if cmd == "b":
        return "balance"
    elif cmd == "s":
        return "spin"
    elif cmd == "h":
        return "help"
    elif cmd == "e":
        return "exit"
    else:
        return cmd


def spin():
    """
    The spin function simulates the slot machine and outputs the winnings
    depending out the resulting spin.
    """

    time.sleep(0.75)

    one = random.randint(1, 9)
    # Note that the "end" parameter ensures that each digit is output on the
    # same line. Additionally, "flush" forces Python to immediately print the
    # value instead of waiting to batch together several prints.
    print(one, end=" ", flush=True)
    time.sleep(SPIN_PAUSE_INTERVAL)

    two = random.randint(1, 9)
    print(two, end=" ", flush=True)
    time.sleep(SPIN_PAUSE_INTERVAL)

    three = random.randint(1, 9)
    print(three, flush=True)
    time.sleep(SPIN_PAUSE_INTERVAL)

    if one == two and two == three:
        return WINNINGS_FOR_THREE
    elif one == two or two == three or one == three:
        return WINNINGS_FOR_TWO
    else:
        return -SPIN_COST


def show_help():
    print("Python Slot Machine manual")
    print("\t 'balance' or 'b' \t -> print the user's current balance")
    print("\t 'spin' or 's'  \t -> initiate a slot machine spin")
    print("\t 'help' or 'h'  \t -> print this information")
    print("\t 'exit' or 'e'  \t -> exit the current session")


if __name__ == "__main__":
    main()
