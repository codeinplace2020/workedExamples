import math


def main():
    # This program allows users to repeatedly approximate the value of pi through three infinite series approaches
    # The only inputed argument is the number of iterations - the more iterations, the more accurate the result!
    while True:
        # Read the iterations in from the user. Type is integer
        iterations = int(input("Enter number of iterations for estimation algorithms: "))

        # Display different calculations to the user
        print("The Pi estimation is...")
        print("According to Leibniz: ", leibniz_pi(iterations))
        print("According to Nilakantha: ", nilakantha_pi(iterations))
        print("According to Newton: ", newton_pi(iterations))
        print("")


def leibniz_pi(x):
    # Leibniz used this approximation in 1674:
    # 4 / 1 - 4 / 3 + 4 / 5 - 4 / 7 + 4 / 9 - ...
    p = 0.0
    for i in range(1, x + 1):
        p = p + ((-1 * math.pow(-1, i)) * 4 / (2 * i - 1))
    return p


def nilakantha_pi(x):
    # An infinite series for PI published by Nilakantha in the 15th century goes as follows:
    # 3 + (4 / 2 * 3 * 4) - (4 / 4 * 5 * 6) + (4 / 6 * 7 * 8) - ...
    p = 3.0
    for i in range(1, x + 1):
        if i == 1:
            p = 3.0
        else:
            p = p + ((math.pow(-1, i)) * 4 / (((i - 1) * 2) * (((i - 1) * 2) + 1) * (((i - 1) * 2) + 2)))
    return p


def newton_pi(x):
    # One of the simpler methods Newton used was to refine the ratio between sine and cosine in a circle
    old = 3.0
    new = old - (math.sin(old)) / (math.cos(old))
    while x != 0:
        old = new
        new = old - (math.sin(old)) / (math.cos(old))
        x -= 1
    return new


if __name__ == '__main__':
    main()
