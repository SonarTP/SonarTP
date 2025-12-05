def retone():
    return 1

class Jeu:
    def __init__(self):
        self.plateau = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_'],
    ]
        self.last_player = False

    def play(self, x, y):
        assert x in [1, 2, 3]
        assert y in [1, 2, 3]
        assert self.plateau[y-1][x-1] == '_'
        if self.last_player:
            self.plateau[y-1][x-1] = 'X'
        else:
            self.plateau[y-1][x-1] = 'O'
        self.last_player = not self.last_player

    def check_win(self, x, y):
        play = self.plateau[y-1][x-1]
        for i in range(1, 3):
            if self.plateau[(y-1+i)%3][x-1] != play:
                break
            return True
        for j in range(1, 3):
            if self.plateau[y-1][(x-1+j)%3] != play:
                break
            return True
        return False

    def __repr__(self):
        repr = '\n-Jeu-\n'
        repr += '\n'.join([' '.join(line) for line in self.plateau])
        return repr + '\n'

if __name__=='__main__':
    jeu = Jeu()
    for i in range(5):
        jeu.play(i%2+1, i//2+1)
        print(jeu)
