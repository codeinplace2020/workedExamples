import math

"""
This program reads the lengths of the sides AB and AC of a right triangle ABC with
 its right angle located at A, and outputs the the followings:
 - cos(ABC)
 - sin(ABC)
 - cos(ABC)^2 + sin(ABC)^2
 
 The last quantity, known as the Pythagorean identity is always equal to 1. Due to
 numerical precision errors, the program may display values slightly greater than 
 or less than 1.
"""

def main():
	while True:
		# Read the mass in from the user. type is float
		ab = float(input("Enter the length of AB: "))
		ac = float(input("Enter the length of AC: "))
		bc = math.sqrt(ab**2 + ac**2)
		cos_abc = ab/bc
		sin_abc = ac/bc
		sum_squared = cos_abc**2 + sin_abc**2
		print("cos(ABC) = " + str(cos_abc))
		print("sin(ABC) = " + str(sin_abc))
		print("cos(ABC)^2 + sin(ABC)^2= " + str(sum_squared))
		print("")


if __name__ == '__main__':
	main()