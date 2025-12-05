def retone():
    return 1

class Plateau:
    def __init__(self):
        self.plateau = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
        self.last_player = False

    def play(self, x, y):
        assert x in [1, 2, 3]
        assert y in [1, 2, 3]
        assert self.plateau[x-1][y-1] == ' '
        if self.last_player:
            self.plateau[x-1][y-1] = 'X'
        else:
            self.plateau[x-1][y-1] = 'O'
        self.last_player = not self.last_player
