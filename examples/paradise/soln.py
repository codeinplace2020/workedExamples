import random
import time

P_BURGER = 4.99 
P_FRIES = 2.99
P_SODA = 1.99
P_PIECH = 3.14
MIN_SAHAMI = 1.62
MAX_SAHAMI = 2.72

def main():
    welcome()
    menu()
    order()

def welcome():
    print('Welcome to Programmer\'s Paradise!')
    print('----------')
    time.sleep(1)

def menu():
    print('Here\'s our menu:')
    print()
    time.sleep(1)
    print('Boolean Burger: $' + str(P_BURGER))
    time.sleep(1)
    print('Function Fries: $' + str(P_FRIES))
    time.sleep(1)
    print('String Soda: $' + str(P_SODA))
    time.sleep(1)
    print()
    

def secret_menu():
    print('----------')
    print('Here\'s our secret menu:')
    time.sleep(1)
    print()
    print('Piech Perfection: $' + str(P_PIECH))
    time.sleep(1)
    print('Sahami Special: $' + str(MIN_SAHAMI) + '-$' + str(MAX_SAHAMI))
    time.sleep(1)
    print()

def order():
    print('What can I get for you?')
    count = 1
    total = 0
    item = input('1. ')
    while item != '':
        if item == 'Boolean Burger':
            total += P_BURGER
        elif item == 'Function Fries':
            total += P_FRIES
        elif item == 'String Soda':
            total += P_SODA
        elif item == 'Secret Menu Please!':
            secret_menu()
            count -= 1
        elif item == 'Piech Perfection':
            total += P_PIECH
        elif item == 'Sahami Special':
            total += random.uniform(MIN_SAHAMI, MAX_SAHAMI)
        else:
            print('Please enter a valid item.')
            count -= 1
        count += 1
        item = input(str(count) + '. ')
    
    print()
    print('Your total is...')
    time.sleep(1)
    print('$' + "%.2f" % round(total, 2))
    time.sleep(1)
    print()
    print('Thank you for choosing Programmer\'s Paradise.')
    time.sleep(1)
    print('We hope you loop by again!')
    time.sleep(1)
    print()
    exit()

if __name__ == '__main__':
    main()