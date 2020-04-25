

def main():
    while True:
        # Read the mass in from the user. type is float
        mass_in_kg = float(input("Enter kilos of mass: "))
        height_in_meter = float(input("Enter height in meter: "))

        # Calculate BMI
        # equivalently bmi = m/h^2
        bmi = mass_in_kg / (height_in_meter * height_in_meter)

        if bmi < 18.5:
            bmi_category = "Underweight"
        elif bmi < 25:
            bmi_category = "Normal Weight"
        elif bmi < 30:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"

        # Display work to the user
        print("BMI = m / h ^ 2...")
        print("m = " + str(mass_in_kg) + " kg")
        print("h = " + str(height_in_meter) + " m")
        print("BMI is: " + str(bmi) + " kg/m^2")
        print("BMI category is: ", bmi_category)


if __name__ == '__main__':
    main()
