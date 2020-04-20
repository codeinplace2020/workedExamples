
def fahrenheit_to_celsius():
    # get the fahrenheit temperature from the user
    fahrenheit = float(input("Enter Temperature in Fahrenheit : "))
    # use the formula to calculate temperature in celsius
    celsius = (fahrenheit - 32) * 5.0/9.0
    # output with appropriate units
    print("Temperature:" + str(fahrenheit) + "F = " + str(celsius) + "C")

def celsius_to_fahrenheit():
    # get the celsius temperature from the user
    celsius = float(input("Enter Temperature in Celsius : "))
    # use the formula to calculate temperature in fahrenheit
    fahrenheit = (celsius * 9.0/5.0) + 32
    # output with appropriate units
    print("Temperature:" + str(celsius) +  "C = " + str(fahrenheit) + "F")

def main():
    # get the choice from the user
    option = int(input("Enter choice (1/2): \n1. Fahrenheit to Celsius \n2. Celsius to Fahrenheit \n"))

    # based on the option call the appropriate function
    # if the user enters an invalid option print the appropriate response
    if option==1:
        fahrenheit_to_celsius()
    elif option==2:
        celsius_to_fahrenheit()
    else:
        print("INVALID OPTION!")

if __name__ == '__main__':
    main()
