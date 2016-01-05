# -*- coding: utf-8 -*-

class Heuristic1Player(object):
    """Implementa a herística que leva em conta a
    quantidade de peças que cada um vai ter"""

    def __init__(self, color):
        self.color = color

    def play(self, board):
        from models.minimax_alfabeta import MiniMaxAlfaBeta
        from models.players.heuristics import heuristic_corners_and_bad_corners
        depth = 3
        minimax = MiniMaxAlfaBeta(depth)
        minimax.mini_max_alfa_beta(
            board,
            depth,
            self.color,
            float('-inf'),
            float('inf'),
            True,
            heuristic_corners_and_bad_corners
        )

        return minimax.chosen_move
