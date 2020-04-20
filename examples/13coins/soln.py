import random

NUM_COINS = 13
NUM_WEIGHING = 3 # Theoretical minimum = math.ceil(math.log(2*NUM_COINS+1, 3))


def main():
    # Welcome message
    print(f'Welcome to the game of {NUM_COINS} coins!')
    print('All but one coin has the same weight. The defective coin')
    print(f'is either heavier or lighter. You have {NUM_WEIGHING} chances to')
    print('weigh them using a balance, and you will answer which')
    print(f'coin is defective (coins labeled 1 to {NUM_COINS}).')
    
    # Initialize weights: 0 for normal coin, -1/+1 for defective coin
    bad_coin = 1#random.randint(0, NUM_COINS-1)
    bad_weight = random.choice((-1,1))
    weights = [0 if i != bad_coin else bad_weight for i in range(NUM_COINS)]

    # Weighing
    for i in range(NUM_WEIGHING):
        print(f'\n=== Weighing Round #{i+1} ===')
        weigh_coins(weights)

    # Getting answer
    answer = int(input(f'\nWhich coin is defective (enter 1 to {NUM_COINS})? ')) - 1
    if bad_coin == answer:
        print('Congratulations!')
    else:
        print(f'Sorry, the defective coin is #{bad_coin+1}.')


def weigh_coins(weights):
    weight_left = weigh_one_side(weights,'left')
    weight_right = weigh_one_side(weights,'right')
    if weight_left == weight_right:
        print('Two sides have the same weights.')
    elif weight_left < weight_right:
        print('The left side is lighter.')
    else:
        print('The left side is heavier.')
    

def weigh_one_side(weights, side):
    weight = 0
    while True:
        coin = input(f'Select coins on the {side} (press Enter when done): ')
        if coin == '':
            break
        weight += weights[int(coin)-1]
    return weight


if __name__ == '__main__':
    main()
