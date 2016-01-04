# -*- coding: utf-8 -*-
from models.minimax_alfabeta import MiniMaxAlfaBeta


def heuristic_value(board, color):
    """Corners Captured
    Recebe um tabuleiro e uma cor de jogador
    Retorna a quantidade de movimentos que a cor especificada tem
    """
    my_color = color
    enemy_color = board._opponent(my_color)
    my_valid_moves = len(board.valid_moves(color))
    enemy_valid_moves = len(board.valid_moves(enemy_color))

    numerator = my_valid_moves - enemy_valid_moves
    denominator = my_valid_moves + enemy_valid_moves
    heuristic = int(100 * numerator/denominator)

    return heuristic


class Heuristic4Player(object):
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

a_fix_for_globals_order = Heuristic4Player
