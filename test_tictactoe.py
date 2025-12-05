import tictactoe

def test_retone():
    assert tictactoe.retone() == 1

def test_init():
    jeu = tictactoe.Jeu()
    assert jeu.plateau == [[' '] * 3] * 3

def test_play():
    jeu = tictactoe.Jeu()
    for i in range(3):
        jeu.play(i+1, 1)
    assert jeu.last_player
    assert jeu.plateau == [
        ['O', ' ', ' '],
        ['X', ' ', ' '],
        ['O', ' ', ' '],
    ]