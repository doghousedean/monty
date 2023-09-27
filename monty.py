"""
Dammit this thing is driving me nuts
"""
import random


class Door():

    def __init__(self, type='zonk', state='closed') -> None:
        self.type = type
        self.state = state

    def __str__(self) -> str:
        return f"Type: {self.type} State: {self.state}"

    def __repr__(self) -> str:
        return f"Door('{self.type}', '{self.state}')"


class Monty():

    def __init__(self, doors=3) -> None:
        self._doors = [Door() for _ in range(0, doors)]
        self._monty = None
        self._player = None
        self._car = None
        self._choose_car()
        self._player_choice()
        self._set_monty()
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
        # doors.pop(doors.index(random.choice(doors)))
        for each_door in [door for door in doors if door != self._monty]:
            self._open_door(each_door)

    def doors(self) -> list:
        return [repr(door) for door in self._doors]


if __name__ == "__main__":
    max_runs = 1000
    max_doors = 100
    wins = 0
    for _ in range(0, max_runs):
        m = Monty(max_doors)
        if m._monty.type == 'car':
            wins += 1
        print(
            f"Player's Door: {m._player.type}, Monty's Door: {m._monty.type}")
        # print([door.type for door in m._doors])
    print("="*60)
    print(f"Max Runs: {max_runs} Max Doors: {max_doors}")
    print(
        f"Chances: Player: {(1/max_doors) * 100}% Always_switch: {(1-(1/max_doors)) * 100}%")
    print(f"Win Rate {(wins/max_runs) * 100}%")
    print("="*60)
