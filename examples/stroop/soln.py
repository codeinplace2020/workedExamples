import random
import time
from colorama import init
from termcolor import colored
init(autoreset=True)


def main():
    #call the print_intro funcion
    print_intro()

    #assign the random_color_name functin to a variable
    color_name = random_color_name()
    print(' ')
    #call the print_in_color function and set the color_name to match the color of ink the color name would be printed in
    #e.g if color_name is 'green', print the font 'green' in green ink
    print_in_color(color_name , font_color= color_name)
    response = input('What color ink is the word written in? ')
    if response != color_name:
            print('Correct answer was: ' + color_name)
    return response == color_name


def print_intro():
    '''
    Function: print intro
    Prints a simple welcome message
    '''
    print('This is the Stroop test! Name the font-color used:')
    #print_in_color('text', 'color')
    print_in_color('red', 'red')
    print_in_color('blue', 'blue')
    print_in_color('pink', 'pink')
    print_in_color('green', 'green')

def random_color_name():
    '''
    Function: random color
    Returns a string (either red, blue, pink or green) with equal likelihood
    '''
    return random.choice(['red', 'blue', 'pink', 'green'])

def print_in_color(text, font_color):
    '''
    Function: print in color
    Just like "print" but this time, you can specify the font-color
    '''
    if font_color == 'pink': # magenta is a lot to type...
        font_color = 'magenta' #another way of saying if the font color is pink, print the fonts in magenta ink
    print(colored(text, font_color, attrs=['bold']))


if __name__ == '__main__':
    main()