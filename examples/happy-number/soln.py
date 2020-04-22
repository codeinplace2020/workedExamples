def main():
	while True:
		# Read the number in from the user. type is int
		number = int(input("Enter the number to test: "))
		current_number = number
		i = 0
		# We loop if we havent reached 1 and made less than 100 computations
		while int(current_number) != 1 and i < 100:
			new_number = 0
			output = ""
			# We loop over every digits of the current number
			for coef in str(current_number):
				new_number = new_number + int(coef) ** 2
				output = output + str(coef) + "²+"
			# We remove the last "+" character
			output = remove_last_character(output)
			print(output + "=" + str(new_number))
			current_number = str(new_number)
			i = i + 1

		if int(current_number) == 1:
			print("Number " + str(number) + " is a happy number")
		else:
			print("Number " + str(number) + " is not a happy number")


def remove_last_character(sentence):
	"""
	Remove the last character of a string
	Parameters:
	sentence (str): a string sentence
	Returns:
	str:Returning truncated sentence
	"""
	return sentence[:-1]


if __name__ == '__main__':
	main()