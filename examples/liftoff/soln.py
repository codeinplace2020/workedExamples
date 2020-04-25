#a program that works like a countdown call
#the countdown runs from 10 -1 and then prints 'Liftoff'

#define your function
def main():

    #we use a for loop and the range funstion which has this format
    #range(start, stop, step)
    #start - starting value
    #stop - stopping value
    #step - format of printing the generated numbers
    #we set the step value to a negative index so the countdown starts printing from the last
    #number in the range (10) and stops at the first number (1)
    for num in range(10,0,-1):

        #we print out the 'num' values in the range
        print(num)

    #we print 'LIFTOFF!' outside of the loop so it appears at the end of the countdown and not
    #inside the countdown sequence
    print('Liftoff!')

#call your function
if __name__ == '__main__':
    main()

