# -*- coding: utf-8 -*-
from models.move import Move

class MiniMaxAlfaBeta(object):

    def __init__(self):
        self.chosen_move = None

    def mini_max_alfa_beta(self, board, depth, color, parent_alfa, parent_beta, max_gamer, heuristic_function):
        """
        """
        if(depth == 0):
            heuristic_value = heuristic_function(board, color)
            return heuristic_value


        alfa = float('-inf')
        beta = float('inf')
        enemy_color = board._opponent(color)
        valid_moves = board.valid_moves(color)
        for valid_move in valid_moves:
            board_copy = board.get_clone()
            move = Move(valid_move)
            board_copy.play(move, color)
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
                alfa = max(best_value, alfa)
                my_best_value = alfa
                if my_best_value > parent_beta:
                    break
            else:
                beta = min(best_value, beta)
                my_best_value = beta
                if my_best_value < parent_alfa:
                    break

            # self.chosen_move = valid_move

        return my_best_value




