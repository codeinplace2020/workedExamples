# a python program that randomly generates simple addition problems for the user,
# reads in the answer from the user,
# and then checks to see if they got it right or wrong,
# until the user appears to have mastered the material.

#import the random library
import random

#define your function
def main():

    #we set the number of iterations to 0 as our starting value
    iteration = 0

    #we use a while loop so the keeps running as long as the user defined conditions are true
    while True:

        #since we want the program to end after 3 correct consecutive answers,
        #we state this condition in an 'if' statement
        if iteration == 3:
            print('Congratulations! You mastered addition.')

            #'break' keyword breaks out of the loop (ends the program)
            break

        #if the 'if' block above is wrong, the 'else' code block would run
        else:
            num_one = random.randint(10, 99)
            num_two = random.randint(10, 99)
            result = num_one + num_two

            #we use the f formatting to set values of the variable names in curly brackets at
            #the appropriate positions
            print(f'What is {num_one} + {num_two}?')

            #we enable the user type in their answers and we convert it to a float using the
            #'float' keyword
            answer = float(input('Your answer: '))

        #we define conditions to test the correctness of the user's input (answer)
        if answer == result:

            #we increase the value of our iteration (we increase the starting value by 1)
            iteration += 1

            #the use of '/' is called escaping. It is used to inform the interpreter that,
            #the character is part of a string
            print(f'Correct! You\'ve gotten {iteration} correct in a row.')

        else:
            print(f'Incorrect. The expected answer is {result}.')

            #the interation value is reduced by one, so the iteration starts counting all over from 1,
            #when the if block above is true
            iteration -= iteration

#call your function
if __name__ == '__main__':
    main()