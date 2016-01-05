# -*- coding: utf-8 -*-
from models.players.utils import get_gamephase, PHASE_OPENING, PHASE_MIDGAME, PHASE_ENDGAME


def heuristic_coins_qtd(board, color):
    """Recebe um tabuleiro e uma cor de jogador
    Retorna a quantidade de peças que a cor especificada tem
    """
    heuristic = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if board.board[i][j] == color:
                heuristic += 1

    return heuristic


def heuristic_coin_parity(board, color):
    """Coin Parity
    Recebe um tabuleiro e uma cor de jogador
    Retorna a quantidade de peças que a cor especificada tem
    """
    my_color = color
    enemy_color = board._opponent(my_color)
    my_coins = 0
    opponent_coins = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if board.board[i][j] == my_color:
                my_coins += 1
            if board.board[i][j] == enemy_color:
                opponent_coins += 1

    numerator = my_coins - opponent_coins
    denominator = my_coins + opponent_coins
    if denominator == 0:
        return 0

    heuristic = int(100 * numerator/denominator)

    return heuristic


def heuristic_mobility(board, color):
    """Mobility
    Recebe um tabuleiro e uma cor de jogador
    Retorna a quantidade de movimentos que a cor especificada tem
    """
    my_color = color
    enemy_color = board._opponent(my_color)
    my_valid_moves = len(board.valid_moves(color))
    enemy_valid_moves = len(board.valid_moves(enemy_color))

    numerator = my_valid_moves - enemy_valid_moves
    denominator = my_valid_moves + enemy_valid_moves
    if denominator == 0:
        return 0

    heuristic = int(100 * numerator/denominator)

    return heuristic


def heuristic_corners_captured(board, color):
    """Corners Captured
    Recebe um tabuleiro e uma cor de jogador
    Retorna a quantidade de movimentos que a cor especificada tem
    """
    corners = [
        [1, 1],
        [1, 8],
        [8, 1],
        [8, 8]
    ]
    enemy_color = board._opponent(color)

    my_total_corners = 0
    enemy_total_corners = 0

    for corner in corners:
        row = corner[0]
        col = corner[1]
        if board.board[row][col] == color:
            my_total_corners += 1
        elif board.board[row][col] == enemy_color:
            enemy_total_corners += 1

    numerator = my_total_corners - enemy_total_corners
    denominator = my_total_corners + enemy_total_corners
    if denominator == 0:
        return 0

    heuristic = int(100 * numerator/denominator)

    return heuristic


def get_bad_corners_for_corner(corner):
    if corner == [1, 1]:
        return [[1, 2], [2, 2], [2, 1]]

    if corner == [8, 8]:
        return [[8, 7], [7, 7], [7, 8]]

    if corner == [1, 8]:
        return [[1, 7], [2, 7], [2, 8]]

    if corner == [8, 1]:
        return [[7, 1], [7, 2], [8, 2]]


def heuristic_corners_and_bad_corners(board, color):

    corners = [
        [1, 1],
        [1, 8],
        [8, 1],
        [8, 8]
    ]
    enemy_color = board._opponent(color)

    my_total_corners = 0
    enemy_total_corners = 0
    bad_corners = 0

    for corner in corners:
        row = corner[0]
        col = corner[1]
        if board.board[row][col] == color:
            my_total_corners += 1
        elif board.board[row][col] == enemy_color:
            enemy_total_corners += 1
        else:
            for bad_corner in get_bad_corners_for_corner(corner):
                if board.board[bad_corner[0]][bad_corner[1]] == color:
                    bad_corners += 1

    numerator = my_total_corners - enemy_total_corners - bad_corners
    denominator = my_total_corners + enemy_total_corners + bad_corners
    if denominator == 0:
        return 0

    heuristic = int(100 * numerator/denominator)

    return heuristic


def heuristic_stability(board, color):
    """
    """
    heuristic_weights = [
        [4, -3, 2, 2, 2, 2, -3, 4],
        [-3, -4, -1, -1, -1, -1, -4, -3],
        [2, -1, 1, 0, 0, 1, -1, 2],
        [2, -1, 0, 1, 1, 0, -1, 2],
        [2, -1, 0, 1, 1, 0, -1, 2],
        [2, -1, 1, 0, 0, 1, -1, 2],
        [-3, -4, -1, -1, -1, -1, -4, -3],
        [4, -3, 2, 2, 2, 2, -3, 4],
    ]
    enemy_color = board._opponent(color)

    my_total_stability = 0
    enemy_total_stability = 0

    for i in range(1, 9):
        for j in range(1, 9):
            if board.board[i][j] == color:
                my_total_stability += heuristic_weights[i-1][j-1]
            elif board.board[i][j] == enemy_color:
                enemy_total_stability += heuristic_weights[i-1][j-1]

    numerator = my_total_stability - enemy_total_stability
    denominator = my_total_stability + enemy_total_stability
    if denominator == 0:
        return 0

    heuristic = int(100 * numerator/denominator)

    return heuristic


def combined_heuristics_value(board, color):

    heuristic = 0
    current_phase = get_gamephase(board)

    if current_phase == PHASE_OPENING:
        heuristic += 2 * heuristic_mobility(board, color)
        heuristic += 1 * heuristic_corners_and_bad_corners(board, color)
        heuristic += 1 * heuristic_corners_captured(board, color)
        heuristic += 6 * heuristic_stability(board, color)

    elif current_phase == PHASE_MIDGAME:

        heuristic += 1 * heuristic_mobility(board, color)
        heuristic += 3 * heuristic_corners_and_bad_corners(board, color)
        heuristic += 1 * heuristic_corners_captured(board, color)

        if color == board.BLACK:
            heuristic += 3 * heuristic_stability(board, color)
            heuristic += 1 * heuristic_coin_parity(board, color)
        else:
            heuristic += 3.2 * heuristic_stability(board, color)
            heuristic += 0.8 * heuristic_coin_parity(board, color)

    else:
        heuristic += 3 * heuristic_coin_parity(board, color)
        heuristic += 2 * heuristic_stability(board, color)
        heuristic += 3 * heuristic_corners_and_bad_corners(board, color)
        heuristic += 2 * heuristic_mobility(board, color)

    return heuristic
