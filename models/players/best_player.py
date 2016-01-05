# -*- coding: utf-8 -*-


class BestPlayer(object):

    """
    Heuristicas combinadas
    """

    def __init__(self, color):
        self.color = color

    def play(self, board):
        from models.minimax_alfabeta import MiniMaxAlfaBeta
        from models.players.heuristics import combined_heuristics_value
        from models.players.heuristics import get_gamephase
        print ">>>phase: %d" % get_gamephase(board)
        depth = 3
        minimax = MiniMaxAlfaBeta(depth, )
        minimax.mini_max_alfa_beta(
            board,
            depth,
            self.color,
            float('-inf'),
            float('inf'),
            True,
            combined_heuristics_value
        )

        return minimax.chosen_move
