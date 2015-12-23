# -*- coding: utf-8 -*-
import copy
from models.move import Move
from models.board import Board as board
from models.minimax_alfabeta import MiniMaxAlfaBeta


def heuristic_value(board, color):
    """Recebe um tabuleiro e uma cor de jogador
    Retorna a quantidade de peças que a cor especificada tem
    """
    heuristic = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if board.board[i][j] == color:
                heuristic += 1

    return heuristic

class Heuristic1Player(object):
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


    # def build_game_tree(self, board):
    #     valid_moves = board.valid_moves(self.color)
    #     heuristic = 0
    #     chosen_move = []
    #     for valid_move in valid_moves:
    #         board_copy = copy.deepcopy(board)
    #         move = Move(valid_move)
    #         board_copy.play(move, self.color)
    #         heuristic_value = heuristic_value(board_copy, self.color)
    #         if(heuristic_value > heuristic):
    #             heuristic = heuristic_value
    #             chosen_move = move

a_fix_for_globals_order = Heuristic1Player