C = 299792458
	
def main():
	while True:
		# Read the mass in from the user. type is float
		mass_in_kg = float(input("Enter kilos of mass: "))
		
		# Calculate energy
		# equivalently energy = mass * (C ** 2)
		# using the ** operator
		energy_in_joules = mass_in_kg * C * C
		
		# Display work to the user
		print("e = m * C^2...")
		print("m = " + str(mass_in_kg) + " kg")
		print("C = " + str(C) + " m/s")
		print(str(energy_in_joules) + " joules of energy!")
		print("")

if __name__ == '__main__':
	main()