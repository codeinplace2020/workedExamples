#subtract numbers
#a python script which accepts two numbers from the user,
#and subtracts the second from the first

#define the function
def main():
    #print the title of the program
    print('This program subtracts one number from another.')

    #accept the first input
    #float keyword converts the input to a decimal number for uniformity
    first_number = float(input('Enter first number: '))

    #accept the second input
    second_number = float(input('Enter second number: '))

    #subtract the second input from the first input
    result = first_number - second_number

    #i used f string formatting to display the final answer in a format that's more readable
    #the variable name holding my answer to the subtraction is put in a curly bracket and placed at the
    #position where i want it to be
    print(f'The result is {result}')

#call your function
if __name__ == '__main__':
    main()

#----------------------------------------------------------
