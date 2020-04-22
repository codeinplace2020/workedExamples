SHEETS = 160
USAGE = 6


def main():
	# This is a while loop (like in python) which never ends!
	while True:
		# Read the amount of Toilet Paper rolls from the user. type is float
		number_of_rolls = float(input("Enter the amount of rolls you have: "))
		toilet_visits = float(input("Enter the number of toilet visits per day: "))

		# Calculate how long will the user's supply last
		# How long = SHEETS * number of rolls mass / (USAGE * toilet visit)
		how_long = int(SHEETS * number_of_rolls / (USAGE * toilet_visits))
		
		# Display work to the user
		print("How long = 160 sheets per roll * number of rolls / (6 sheets per toilet visit * toilet visit per day)...")
		print("Number of rolls = " + str(number_of_rolls) + " rolls")
		print("Toilet visit = " + str(toilet_visits) + " per day")
		print("You will last " + str(how_long) + " days!")
		print("")


if __name__ == '__main__':
	main()