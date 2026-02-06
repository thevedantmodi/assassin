import random


class Player:
    name = str
    email = str

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.email})"


class AssassinGenerator:
    def __init__(self, players):
        self.players = players

    def gen(self, verbose=True):
        random.shuffle(self.players)
        targets = {}

        for i in range(len(self.players)):
            assassin = self.players[i]
            target = self.players[(i + 1) % len(self.players)]
            targets.update({assassin: target})

        if verbose:
            for p, t in targets.items():
                print(f"{p} has a target of {t}")

        return targets

    def generate(self, verbose=True):
        if verbose:
            print("Generating assassin list...")

        targets = self.gen(verbose)
        # check that assignments are ok
        while any(a.name == t.name for a, t in targets.items()):
            targets = self.gen()

        return targets
