import tictactoe

def test_retone():
    assert tictactoe.retone() == 1

def test_init():
    jeu = tictactoe.Jeu()
    assert jeu.plateau == [['_'] * 3] * 3

def test_play():
    jeu = tictactoe.Jeu()
    for i in range(3):
        jeu.play(i+1, 1)
    assert jeu.last_player
    assert jeu.plateau == [
        ['O', 'X', 'O'],
        ['_', '_', '_'],
        ['_', '_', '_'],
    ]

def test_win_vertical():
    jeu = tictactoe.Jeu()
    for i in range(5):
        x, y = i%2 + 1, i//2 + 1
        jeu.play(x, y)
        if i<4:
            assert not jeu.check_win(x, y)
    assert jeu.check_win(x, y)
    
def test_win_horizontal():
    jeu = tictactoe.Jeu()
    for i in range(5):
        x, y = i//2 + 1, i%2 + 1
        jeu.play(x, y)
        if i<4:
            assert not jeu.check_win(x, y)
    assert jeu.check_win(x, y)

def test_false():
    assert False