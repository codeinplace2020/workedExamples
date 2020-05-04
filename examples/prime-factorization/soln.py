"""
This program performs prime factorization onto user-specified positive integers.
"""

def main():
	while True:
		n = read_positive_int("Enter an integer: ")
		show_prime_factors(n)
		print("")


def read_positive_int(prompt_msg):
	"""
	Reads a positive integer entered by the user.

	Args:
		prompt_msg (str): The prompt message to show the user when requesting the input.

	Returns:
		int: The positive integer entered by the user.
	"""
	n = int(input(prompt_msg))
	while n<=0:
		print("Please enter a positive integer")
		n = int(input(prompt_msg))
	
	return n


def show_prime_factors(n):
	"""
	Show the prime factors of n

	Args:
		n (int): The number to be factorized
	"""

	print("The prime factors of " + str(n) + " are: ")
	while n>1:
		p = smallest_prime_factor(n)
		print(p)
		n  = n // p


def smallest_prime_factor(n):
	"""
	Compute the smallest prime factor of n.

	Args:
		n (int): The number to be factorized

	Returns:
		int: The smallest number in the range [2, n] that is 
			a divisor of n, and is a prime number
	"""
	for i in range(2, n+1):
		if n%i == 0 and is_prime(i):
			return i


def is_prime(n):
	"""
	Test if the specified number is prime.

	Args:
		n (int): The number to be tested

	Returns:
		bool: True if n has no divisor in range [2, n[. False otherwise.
	"""
	for d in range(2, n):
		if n%d == 0:
			return False
	return True



if __name__ == '__main__':
	main()