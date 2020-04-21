#a python script that gives random answers to questions being asked by the user

#an inbuilt module that enables the interpreter pick random values from
#a defined range of options
import random

def main():
    print('Type QUIT to end the program')

    #i used a while loop so the program runs until it is stopped by the user
    while True:
        #prompt to tell the user to ask a question
        question = input('Ask me a question: ')

        #conditions under which the program runs
        if question != ' ':

            #we use the random.randint to specify that we are selecting integers between the stated range (start, stop)
            option = random.randint(1,5)
            if option == 1:
                print('A round of applause for yourself!')
            if option == 2:
                print('It is decidedly so.')
            if option == 3:
                print('Keep trying champ')
            if option == 4:
                print('Yes, chamo, you did it')
            if option == 5:
                print('aahhhh, really nice work')

            #stopping criteria, to end the while loop
            if question == 'quit':
                #the break keyword is used to end the while loop
                break

        #if the user hits the spacebar when told to ask a question, the program ends
        else:
            print('ask actual questions, run again')
            break

#call the function
if __name__ == '__main__':
    main()


