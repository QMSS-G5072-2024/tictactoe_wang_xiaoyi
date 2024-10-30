import pytest
from tictactoe_xw3028 import *

# Test 1a: Test initialize_board
def test_initialize_board():
    board = initialize_board()
    assert len(board) == 3, "The board should have 3 rows."
    assert all(len(row) == 3 for row in board), "Each row should have 3 columns."
    for row in board:
        for cell in row:
            assert cell == ' ', "Each cell should be initialized with an empty space."

# Test 1b: Test make_move for valid moves
def test_make_move_valid():
    board = initialize_board()

    # Player 'X' makes a move
    success_X = make_move(board, 1, 1, 'X')
    assert success_X == True, "Player X should be able to place their symbol on an empty cell."
    assert board[1][1] == 'X', "The cell (1, 1) should contain 'X'."

    # Player 'O' makes a move
    success_O = make_move(board, 2, 2, 'O')
    assert success_O == True, "Player O should be able to place their symbol on an empty cell."
    assert board[2][2] == 'O', "The cell (2, 2) should contain 'O'."

