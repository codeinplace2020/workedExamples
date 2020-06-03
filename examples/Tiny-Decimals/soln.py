#script that prints out the numbers between two whole numbers correct to 2 decimal places

def main():
    program_intro()
    start_num = float(input('Enter a starting whole number: '))
    stop_num = float(input('Enter a stopping whole number: '))
    tiny_decimals(start_num, stop_num)

def program_intro():
    print('Hi, welcome! \n This program prints the tiny decimals between two whole numbers \
        \n correct to 2 decimal places \n Kindly type numbers when prompted \
        \n press \'ENTER\' key to prompt the next command ..')

def tiny_decimals(start_num, stop_num):
    #print out the starting number
    print(round(start_num,2))
    #i used a while loop because i do not know how many times my code will
    # run to arrive at the final answer
    while start_num < stop_num:
        #increase the starting number by 0.1
        start_num += 0.01 
        #a condition that ensures numbers lesser than or equal to the stop_num
        #get printed
        if start_num <= stop_num:
            #reassigns the start_num value to a value increased by 0.1
            start_num = start_num
        #a condition to ensure that a number greater than our stopping number does 
        #not get printed out
            if start_num == stop_num:
                break 
            print(round(start_num,2)) #print the numbers to 2 decimal places (for precision)
    print(round(stop_num,2))

if __name__ == '__main__':
    main()
