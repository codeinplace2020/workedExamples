def main():
	print("Welcome to the Quiz! How well do you know Daniel?")
	print("Instructions: select your answer by inputing a, b, or c.")

	# Counter variable to keep track of correct answers
	num_correct = 0

	# Temporary variable to respond to a correct/incorrect answer
	correct_bool = question_1()
	if correct_bool:
		print("That's right!")
		num_correct = num_correct + 1
	else:
		print("That's incorrect...")

	correct_bool = question_2()
	if correct_bool:
		print("That's right!")
		num_correct = num_correct + 1
	else:
		print("That's incorrect...")

	correct_bool = question_3()
	if correct_bool:
		print("That's right!")
		num_correct = num_correct + 1
	else:
		print("That's incorrect...")

	print("--------------------")
	print("That's the end of our quiz!")
	print("Congratulations! You got " + str(num_correct) + " questions right!")

"""
Each question has a correct answer of either a, b, or c.
If the user inputs the correct answer, returns True. Otherwise,
returns False.
"""
def question_1():
	print("########## 1 ##########")
	print("Question 1: what pet does Daniel have?")
	print("a. Dog")
	print("b. Cat")
	print("c. Snake")

	response = input("Type a, b, or c and hit enter: ")
	
	"""
	The correct answer is b!
	This is a clever way to return True or False on one line
	"""
	return response == "b"

def question_2():
	print("########## 2 ##########")
	print("Question 2: which does Daniel hate the most?")
	print("a. Hangnails")
	print("b. Waking up early")
	print("c. Stories with no emotional resolution")

	response = input("Type a, b, or c and hit enter: ")
	
	return response == "c"

def question_3():
	print("########## 3 ##########")
	print("Question 3: what is Daniel doing on a Sunday morning?")
	print("a. Sleeping in")
	print("b. Eating homemade brunch")
	print("c. Working out")

	response = input("Type a, b, or c and hit enter: ")
	
	return response == "a"

if __name__ == '__main__':
	main()