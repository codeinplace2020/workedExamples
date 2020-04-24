# constants
CAT_YRS_MULTIPLIER = 4.9
DOG_YRS_MULTIPLIER = 7.18
ELEPHANT_YRS_MULTIPLIER = 1.13
LION_YRS_MULTIPLIER = 5.64
MONKEY_YRS_MULTIPLIER = 3.95
RABBIT_YRS_MULTIPLIER = 7.9
HAMSTER_YRS_MULTIPLIER = 39.5

def main():
	print('This program converts human years to animal years.')

	# gets two user inputs, the human years to convert and the animal type
	human_yrs_str = input('Human years: ')
	animal_type_str = input('Animal type (options: cat, dog, elephant, lion, monkey, rabbit, hamster): ')
	
	# converts human years to animal years of the animal type specified
	animal_yrs = None

	# casts human_yrs_str, a string type variable, to a float type variable
	human_yrs = float(human_yrs_str)

	# converts human years to animal years based on the animal type input
	if animal_type_str == 'cat':
		animal_yrs = human_yrs * CAT_YRS_MULTIPLIER
	elif animal_type_str == 'dog':
		animal_yrs= human_yrs * DOG_YRS_MULTIPLIER
	elif animal_type_str == 'elephant':
		animal_yrs = human_yrs * ELEPHANT_YRS_MULTIPLIER
	elif animal_type_str == 'lion':
		animal_yrs = human_yrs * LION_YRS_MULTIPLIER
	elif animal_type_str == 'monkey':
		animal_yrs = human_yrs * MONKEY_YRS_MULTIPLIER
	elif animal_type_str == 'rabbit':
		animal_yrs = human_yrs * RABBIT_YRS_MULTIPLIER
	elif animal_type_str == 'hamster':
		animal_yrs = human_yrs * HAMSTER_YRS_MULTIPLIER

	# prints the equivalent animal years for the human year input
	# prints error message in animal type was invalid
	if animal_yrs:
		print(human_yrs_str + ' human years is equal to ' + str(animal_yrs) + ' ' + animal_type_str + ' years.')
	else:
		print('Animal type is invalid.')

if __name__ == '__main__':
	main()