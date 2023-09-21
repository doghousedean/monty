import random


def new_game():
    doors = []
    [doors.append('zonk') for _ in range(0, random.randint(0, 1000))]
    doors[random.randint(0, len(doors) - 1)] = 'car'
    return doors


def game():
    max_tries = 100
    for _ in range(0, max_tries):
        doors = new_game()
        choice = random.randint(0, len(doors) - 1)
        car = doors.index('car')
        mh = random.randint(0, len(doors) - 1)
        if doors[mh] == 'car':
            print(
                f"RUN: {_:>5} CAR: {car:>5} MH: {mh:>5} CHOICE: {choice:>5} DOORS: {len(doors):>5} OPENED:{doors[mh]}")


game()
