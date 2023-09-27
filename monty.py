"""
Dammit this thing is driving me nuts
"""
import random
import time


class Door():
    """
        Model for the different door types

        There are doors of zonk and car with state of open or closed
    """

    def __init__(self, type='zonk', state='closed') -> None:
        self.type = type
        self.state = state

    def __str__(self) -> str:
        return f"Type: {self.type} State: {self.state}"

    def __repr__(self) -> str:
        return f"Door('{self.type}', '{self.state}')"


class Monty():
    """
        Model for the game show process
    """

    def __init__(self, doors=3) -> None:
        # Create a list of doors with 3 being the minimum number
        if doors < 3:
            doors = 3
        self._doors = [Door() for _ in range(0, doors)]
        self._monty = None
        self._player = None
        self._car = None
        # Pick a random door to be the car
        self._choose_car()
        # Pick a random door as the player's choice
        self._player_choice()
        # Monty will pick a door that will either be the car or a zonk if the player chose the car
        self._set_monty()
        # For completeness open the other doors
        self._open_remaining()

    def _random_door(self):
        return random.randint(0, len(self._doors) - 1)

    def _choose_car(self):
        car = self._random_door()
        self._doors[car] = Door('car')
        self._car = self._doors[car]

    def _player_choice(self):
        self._player = self._doors[self._random_door()]

    def _open_door(self, door):
        door.state = 'open'
        return door

    def _set_monty(self):
        if self._player == self._car:
            zonks = self._get_zonks()
            self._monty = zonks[random.randint(0, len(zonks) - 1)]
        else:
            self._monty = self._car

    def _get_zonks(self):
        return [door for door in self._doors if door.type == 'zonk']

    def _open_remaining(self):
        doors = self._get_zonks()
        for each_door in [door for door in doors if door != self._monty]:
            self._open_door(each_door)

    def doors(self) -> list:
        return self._doors


def game(max_runs=1000, max_doors=3):
    # Set up the game and run the simulation
    wins = 0
    for _ in range(0, max_runs):
        m = Monty(max_doors)
        # For this version we are ALWAYS choosing montys choice, if that one is a car we win
        if m._monty.type == 'car':
            wins += 1
    print("="*60)
    print(f"Max Runs: {max_runs} Max Doors: {max_doors}")
    print(
        f"Chances: Player: {round((1/max_doors) * 100, 2)}% Always_switch: {round((1-(1/max_doors)) * 100, 2)}%")
    print(f"Win Rate {round((wins/max_runs) * 100, 2)}%")
    print("-"*60)


if __name__ == "__main__":
    # A simple method to run it multiple times
    # Hit CTRL+c to quit
    while True:
        try:
            game()
            time.sleep(0.1)
        except KeyboardInterrupt:
            print()
            print("="*60)
            print(f"🚗🚗🚗           How many cars did you win?          🚗🚗🚗")
            print("="*60)
            break
