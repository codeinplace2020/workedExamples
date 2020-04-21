import random

PI = 3.14159265358979
# Number of digits after decimal point to be displayed
# Should be less than or equal to 14 for double precision float
DIGITS = 5
RADIUS = 1.0

def main():
    while True:
        num_trials = input('Number of trials (press Enter to quit): ')
        if num_trials == '':
            print('Program has ended.')
            break
        num_trials = int(num_trials)
        pi = estimate_pi(num_trials)
        print(f'Actual value of pi:  {PI:.{DIGITS}f}...')
        print(f'The estimated value: {pi:.{DIGITS}f}')


def estimate_pi(num_trials):
    count_in_circle = 0
    for i in range(num_trials):
        x = random.uniform(-RADIUS, RADIUS)
        y = random.uniform(-RADIUS, RADIUS)
        if x*x + y*y < RADIUS*RADIUS:
            count_in_circle += 1
    return 4.0 * count_in_circle / num_trials


if __name__ == '__main__':
    main()