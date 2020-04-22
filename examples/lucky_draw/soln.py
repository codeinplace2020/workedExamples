import random


def main():
    winner = ''
    num_guests = 0

    while True:
        name = input('Guest name (press Enter when done): ')
        if name == '':
            break
        num_guests += 1
        if random.random() < (1.0/num_guests):
            winner = name

    if num_guests == 0:
        print('Oops, no guest shows up.')
    elif num_guests == 1:
        print(f'Only {winner} comes so {winner} is automatically the winner.')
    else:
        print(f'The lucky winner is {winner} among {num_guests} guests.')


if __name__ == '__main__':
    main()
