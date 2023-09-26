import random


def new_game(max_doors=3):
    doors = []
    [doors.append('zonk') for _ in range(0, random.randint(3, max_doors))]
    try:
        doors[random.randint(0, len(doors) - 1)] = 'car'
    except ValueError as e:
        print(doors)
    return doors


def game():
    max_tries = 1000
    wins = 0
    for _ in range(0, max_tries):
        # Run the game max_tries times
        # create a new game
        doors = new_game()
        # Select a door at random as the players choice
        choice = random.randint(0, len(doors) - 1)
        # get the index of the car
        car = doors.index('car')
        done = False
        while done is False:
            # loop until the random door monty picks is not the same as the player choice
            mh = random.randint(0, len(doors) - 1)
            if mh != choice:
                done = True
        # The rule says you should always pick the Monty Hall door, this means that if the monty door is the car you win
        if doors[mh] == 'car':
            wins += 1
            print(
                f"RUN: {_:>5} WINS: {wins/100:>5} CAR: {car:>5} MH: {mh:>5} CHOICE: {choice:>5} DOORS: {len(doors):>5} OPENED:{doors[mh]}")
    print('='*120)
    print(f"Won {wins} out of {max_tries} ({(wins/max_tries)*100})")


game()
