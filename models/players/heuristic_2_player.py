# -*- coding: utf-8 -*-
from models.minimax_alfabeta import MiniMaxAlfaBeta


def heuristic_value(board, color):
    """Recebe um tabuleiro e uma cor de jogador
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
    heuristic = int(100 * numerator/denominator)

    return heuristic


class Heuristic2Player(object):
    """Implementa a herística que leva em conta a
    quantidade de peças que cada um vai ter"""
    def __init__(self, color):
        self.color = color

    def play(self, board):
        depth = 3
        minimax = MiniMaxAlfaBeta(depth)
        minimax.mini_max_alfa_beta(
            board,
            depth,
            self.color,
            float('-inf'),
            float('inf'),
            True,
            heuristic_value
        )

        return minimax.chosen_move

a_fix_for_globals_order = Heuristic2Player
