def main():
    # Read the Fibonacci series length from user, type is integer
    series_length = int(input("Enter the length of the Fibonacci Series: "))

    # check if user entered a proper integer, if yes then compute the series, else print error
    if series_length > 0:
        compute_fibonacci(series_length)
    else:
        print("Invalid input! Please enter a valid integer")


def compute_fibonacci(series_length):
    """
    calculates Fibonacci series for the given length
    pre-condition: series length is a valid integer > 0
    post-condition: none
    """

    # first Fibonacci number
    f0 = 0
    print(f0)

    if series_length > 1:
        # second Fibonacci number
        f1 = 1
        print(f1)
        # calculate the value from third number onwards
        for i in range(series_length - 2):
            result = f0 + f1
            f0 = f1
            f1 = result
            print(result)


if __name__ == '__main__':
    main()
