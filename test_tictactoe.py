import tictactoe

def test_retone():
    assert tictactoe.retone() == 1

def test_init():
    plateau = tictactoe.Plateau()
    assert plateau.plateau == [[' '] * 3] * 3