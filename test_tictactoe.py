import tictactoe

def test_retone():
    assert tictactoe.retone() == 1

def test_init():
    plateau = tictactoe.Plateau()
    assert plateau.plateau == [[' '] * 3] * 3

def test_play():
    plateau = tictactoe.Plateau()
    for i in range(7):
        plateau.play()
    assert plateau.last_player