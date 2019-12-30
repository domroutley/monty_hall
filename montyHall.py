import random
import argparse

def manual():

    doors = genDoors()

    pick = int(input('Pick a door. [1/2/3] > '))
    if pick not in [1,2,3]:
        print('Need to pick a door between 1 and 3...')
        exit()

    goatDoor, unknownDoor = openDoor(pick, doors)

    print(f'You have picked door {pick}, I open door {goatDoor} and show you it is a goat.')
    switch = input(f'Do you want to switch your choice from door {pick} to door {unknownDoor}? [y/n] > ')

    if switch[0].lower() == 'y':
        x = unknownDoor
        unknownDoor = pick
        pick = x

    for door, what in doors.items():
        print(f'Behind door {door} there was a {what}')

    if doors[pick] == 'car':
        print('YOU WIN!')
    else:
        print('YOU LOOSE')

def openDoor(pick, doors):
    goatDoor = pick
    unknownDoor = pick
    while goatDoor == pick or pick == unknownDoor or goatDoor == unknownDoor or doors[goatDoor] != 'goat':
        goatDoor = random.randint(1,3)
        unknownDoor = random.randint(1,3)
        # print(f'g={goatDoor} - u={unknownDoor}')
    return goatDoor, unknownDoor

def genDoors():
    doors = {1:'goat', 2:'goat', 3:'goat'}
    carDoor = random.randint(1,3)
    doors[carDoor] = 'car'
    return doors

def simulate(runs, switch):
    if switch == 'true':
        switch = True
    else:
        switch = False

    run = 1
    record = {'wins': 0, 'loss': 0}
    while run < runs:
        doors = genDoors()
        pick = random.randint(1,3)
        gDoor, uDoor = openDoor(pick, doors)
        if switch:
            x = uDoor
            uDoor = pick
            pick = x

        if doors[pick] == 'car':
             # print('WIN')
             record['wins'] += 1
        else:
             # print('LOOSE')
             record['loss'] += 1

        run += 1

    return record


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate the monty hall probability problem.')
    parser.add_argument('--simulate_count', nargs='?',
                        help='Simulate the problem a number of times')
    parser.add_argument('--switch', nargs='?', default='true',
                        help='Switch always? [true/false] (Default: true)')
    args = parser.parse_args()

    if args.simulate_count:
        print(simulate(int(args.simulate_count), args.switch))
    else:
        manual()
