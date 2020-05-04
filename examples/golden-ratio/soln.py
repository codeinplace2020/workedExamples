
def main():
	"""
	Show the ratio of consecutive Fibonaccy numbers
	"""
	for i in range(1, 100):
		print(golden(i))


def golden(n):
	"""
	Return the ratio of fibonacci number (n) to fibonacci number (n-1)
	"""
	return fib(n)/fib(n-1)


def fib(n):
	"""
	Compute fibonacci term n
	"""
	a = 1
	b = 1

	for i in range(1, n+1):
		next_element = a + b
		a = b
		b =  next_element
	
	return a 


if __name__ == '__main__':
	main()