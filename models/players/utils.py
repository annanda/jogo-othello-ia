# -*- coding: utf-8 -*-

PHASE_OPENING = 1
PHASE_MIDGAME = 2
PHASE_ENDGAME = 3


def get_empty_cells(board):
    empty_cells = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if board.board[i][j] == board.EMPTY:
                empty_cells += 1

    return empty_cells


def get_gamephase(board):

    if get_empty_cells(board) > 45:
        phase = PHASE_OPENING
    elif get_empty_cells(board) < 13:
        phase = PHASE_ENDGAME
    else:
        phase = PHASE_MIDGAME

    return phase
