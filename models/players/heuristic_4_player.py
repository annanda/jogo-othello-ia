# -*- coding: utf-8 -*-


class Heuristic4Player(object):

    """
    Heuristica de corners Captured
    """

    def __init__(self, color):
        self.color = color

    def play(self, board):
        from models.minimax_alfabeta import MiniMaxAlfaBeta
        from models.players.heuristics import heuristic_corners_captured
        depth = 3
        minimax = MiniMaxAlfaBeta(depth)
        minimax.mini_max_alfa_beta(
            board,
            depth,
            self.color,
            float('-inf'),
            float('inf'),
            True,
            heuristic_corners_captured
        )

        return minimax.chosen_move
