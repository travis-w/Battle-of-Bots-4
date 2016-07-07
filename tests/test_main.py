import pytest
from random import randint
from main import get_pieces, winning_move, find_winning, score_position, find_setup, find_best_avg

def generate_board(empty = False):
    board = []
    for i in range(10):
        row = []
        for j in range(10):
            x = 0 if empty else randint(0,2)
            row.append(x)
        board.append(row)
    return board


def test_empty():
    board = generate_board(True)

    assert len(get_pieces(board, 1)) == 0
    assert len(get_pieces(board, 2)) == 0

def test_winning():
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 2, 2, 2, 2, 0, 0, 0, 0],
             [0, 0, 0, 1, 2, 2, 1, 0, 0, 0],
             [0, 1, 2, 1, 1, 2, 0, 1, 0, 0],
             [0, 2, 2, 1, 2, 1, 1, 0, 0, 0],
             [0, 0, 1, 2, 0, 1, 2, 0, 0, 0],
             [0, 0, 2, 0, 2, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert winning_move(board, (2, 1), 2)
    assert not winning_move(board, (2, 1), 1)

    assert len(find_winning(board, 1)) == 0
    assert find_winning(board, 2) == [(2, 1), (2, 6)]

def test_find_best_avg():
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
             [0, 2, 1, 1, 1, 1, 2, 0, 0, 0],
             [0, 0, 1, 2, 1, 2, 1, 0, 0, 0],
             [0, 0, 0, 2, 1, 2, 0, 2, 0, 0],
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert 1 == 1
