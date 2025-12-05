def retone():
    return 1

class Plateau:
    def __init__(self):
        self.plateau = [[' '] * 3] * 3
        self.last_player = False

    def play(self):
        self.last_player = not self.last_player
