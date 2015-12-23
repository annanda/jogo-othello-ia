# -*- coding: utf-8 -*-
from models.move import Move

class MiniMaxAlfaBeta(object):

    def __init__(self, max_depth):
        self.chosen_move = None
        self.max_depth = max_depth

    def mini_max_alfa_beta(self, board, depth, color, parent_alfa, parent_beta, max_gamer, heuristic_function):
        """
        """
        valid_moves = board.valid_moves(color)

        my_best_value = None
        if depth == 0 or not valid_moves:
            my_best_value = heuristic_function(board, color)
            return my_best_value

        alfa = float('-inf')
        beta = float('inf')
        enemy_color = board._opponent(color)
        for valid_move in valid_moves:
            board_copy = board.get_clone()
            # move = Move(valid_move)
            board_copy.play(valid_move, color)
            best_value = self.mini_max_alfa_beta(
                board_copy,
                depth - 1,
                enemy_color,
                alfa,
                beta,
                not(max_gamer),
                heuristic_function
            )
            if max_gamer:
                if best_value > alfa:
                    alfa = best_value
                    best_move = valid_move
                my_best_value = alfa
                if my_best_value > parent_beta:
                    break
            else:
                beta = min(best_value, beta)
                my_best_value = beta
                if my_best_value < parent_alfa:
                    break

        if depth == self.max_depth:
            self.chosen_move = best_move
        return my_best_value




