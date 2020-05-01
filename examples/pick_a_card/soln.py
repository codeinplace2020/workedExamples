# Standard library import
import random


def main():
	"""
	The purpose of this program is to simulate picking a card randomly
	out of a standard 52-card deck of French playing cards.
	"""
	print("")
	print("Welcome to Pick a Card program! To quit the program, simply press enter")
	print("")
	
	response = input("For suits, would you like symbols instead of text? (enter y/Y for yes, n/N for no): ")

	while response != "": # stop running when the user doesn't enter anything/hits enter

		if response == "y" or response == "Y":
			rank = pick_a_rank()
			suit = pick_a_suit(True) # when we want symbols for suits
			print("The randomly picked card was: " + rank + " of " + suit)

		elif response == "n" or response == "N":
			rank = pick_a_rank()
			suit = pick_a_suit(False) # when we want texts for suits
			print("The randomly picked card was: " + rank + " of " + suit)

		print("") # prints a newline to create spacing
		response = input("For suits, would you like symbols instead of text? (enter y/Y for yes, n/N for no): ")
	
def pick_a_rank():
	"""
	There are thirteen ranks: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King.
	"""
	thirteen_ranks_text = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

	random_rank = random.choice(thirteen_ranks_text)

	return random_rank


def pick_a_suit(symbols_instead_of_text):
	"""
	There are four suits: clubs, diamonds, hearts, and spades.
	random.choice will pick a random element from the list of suits.
	The list of suits will depend on symbols_instead_of_text parameter.
	"""
	if symbols_instead_of_text:
		four_suits_symbols = ["♣", "♦", "♥", "♠"]

		random_suit = random.choice(four_suits_symbols)

		return random_suit

	else:
		four_suits_text = ["Clubs", "Diamonds", "Hearts", "Spades"]

		random_suit = random.choice(four_suits_text)

		return random_suit

if __name__ == "__main__":
	main()
