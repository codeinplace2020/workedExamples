#a python script that converts your weight on earth, to the
#equivalent value of your weight on the moon
#your weight on the moon is 16.5% your weight on earth
#- accept weight as input
#- perform maths operation weight on earth * 16.5 / 100
#- print the answer as, 'your equivalent weight on the moon is ..'
#float accepts decimal numbers
#int accepts integers
#str accepts basically anything numbers to letter to symbols
#eval accepts both integers and floats

def main():
    #- accept weight as input
    weight = eval(input('How much do you weigh?: '))
    #formula: equivalent_moon_weight = weight on earth * 16.5 / 100
    equivalent_moon_weight = (weight * 16.5) / 100
    #- print the answer as, 'your equivalent weight on the moon is ..'
    print(f'Your equivalent weight on the moon is {equivalent_moon_weight}')

if __name__ == '__main__':
    main()
