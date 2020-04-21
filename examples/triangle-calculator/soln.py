import math

def main():

    # Introductory explanation
    print("Welcome to the Triangle Calculator!")
    print("What information do you have about your triangle so far?")
    print("(1) Length of all three sides")
    print("(2) Length of two sides and the angle between them")
    choice = int(input("Please choose 1 or 2: "))

    # Both options 1 and 2 ask for two side lengths
    side_a = float(input("Length of side 1: "))
    side_b = float(input("Length of side 2: "))

    # If we know all three sides
    if choice == 1:
        side_c = float(input("Length of side 3: "))

        # Add up all the sides to get the perimeter, divide by 2 for semiperimeter!
        perimeter = side_a + side_b + side_c
        semiperimeter = perimeter / 2

        # This is Heron's Formula for finding the area of a triangle using three sides
        area = math.sqrt(semiperimeter * (semiperimeter - side_a) * (semiperimeter - side_b) *
        (semiperimeter - side_c))

    # If we know the angle between the two sides
    else:
        angle_opposite_c = float(input("Angle between them in degrees: "))

        # Convert into radians
        angle_opposite_c = angle_opposite_c * math.pi / 180

        # The area of a triangle is 1/2 * a * b * sin(C)
        area = 1/2 * side_a * side_b * math.sin(angle_opposite_c)

        # Law of Cosines
        side_c = math.sqrt((side_a * side_a) + (side_b * side_b) -
        (2 * side_a * side_b * math.cos(angle_opposite_c)))

        # Now that we have all the sides, we can find the perimeter
        perimeter = side_a + side_b + side_c

    print("---")
    print("Information about your triangle...")
    print("Side 1: ", side_a)
    print("Side 2: ", side_b)
    print("Side 3: ", side_c)
    print("Perimeter: ", perimeter)
    print("Area: ", area)
    print("---")

if __name__ == "__main__":
    main()
