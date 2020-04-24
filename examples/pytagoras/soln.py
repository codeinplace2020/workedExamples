import math

def main():
	while True:
		# Read the mass in from the user. type is float
		ab = float(input("Enter the length of AB: "))
		ac = float(input("Enter the length of AC: "))
		bc = math.sqrt(ab**2 + ac**2)
		print("The length of BC (the hypotenuse) is: " + str(bc))
		print("")


if __name__ == '__main__':
	main()