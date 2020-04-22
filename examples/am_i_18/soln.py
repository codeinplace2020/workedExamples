AGE_LIMIT = 18

def main():
    age_str = input("Enter your age: ")
    age = int(age_str)
    if age >= AGE_LIMIT:
        print("You're old enough to vote!")
    else:
        print("Sorry, you can't vote yet!")
    print('')

if __name__ == '__main__':
    main()