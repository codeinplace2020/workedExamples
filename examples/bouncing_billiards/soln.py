SCHEMATIC = r'''
              wall
               ||                 <-- v2
               ||      v1       __________
               ||   ________    |        |
               ||   |      |    |   m2   |
               ||   |  m1  |    |        |
               ||   |______|    |________|
               ||================================
                      frictionless floor'''

def main():
    welcome_message()
    while True:
        m1, v1, m2, v2 = init()
        num_collisions = play(m1, v1, m2, v2)
        if num_collisions >= 2:
            print(f"There were {num_collisions} collisions in total.")
        else:
            print(f"There was {num_collisions} collision.")
        if input("Continue? (y or n) ") == 'n':
            print("Program has ended.")
            break


def play(m1, v1, m2, v2):
    print("Bouncing started...", end = '')
    num_collisions = 0
    while has_more_collision(v1, v2):
        if num_collisions%2 == 0: # Collision between blocks
            v1, v2 = solve_velocities(m1, v1, m2, v2)
        else: # Collision between wall and block 1
            v1 *= -1
        num_collisions += 1
    return num_collisions


def solve_velocities(m1, v1, m2, v2):
    v1_new = (m1-m2)/(m1+m2)*v1 + 2*m2/(m1+m2)*v2
    v2_new = 2*m1/(m1+m2)*v1 + (m2-m1)/(m1+m2)*v2
    return (v1_new, v2_new)


def has_more_collision(v1, v2):
    return not (v1 >= 0 and v2 >= 0 and v1 <= v2)


def welcome_message():
    print("Let's play billiard balls! As shown in the schematic below,")
    print("block 1 starts at rest, while block 2 starts with an initial")
    print("velocity. Negative velocity indicates movement to the left.")
    print(SCHEMATIC)


def init():
    print('')
    m1 = float(input('Mass of block 1 [kg]: '))
    m2 = float(input('Mass of block 2 [kg]: '))
    v1 = 0.0
    v2 = float(input('Starting velocity of block 2 [m/s]: '))
    return (m1, v1, m2, v2)


if __name__ == '__main__':
    main()
