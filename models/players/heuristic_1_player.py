# -*- coding: utf-8 -*-
import copy
from models.move import Move
from models.board import Board as board


class Heuristic1Player(object):
    """Implementa a herística que leva em conta a
    quantidade de peças que cada um vai ter"""
    def __init__(self, color):
        self.color = color

    def play(self, board):

        chosen_row = 1
        chosen_colunm = 6
        move = Move(chosen_row, chosen_colunm)
        return move

    def heuristic_value(self, board, color):
        """Recebe um tabuleiro e uma cor de jogador
        Retorna a quantidade de peças que a cor especificada tem
        """
        heuristic = 0
        for i in range(1, 9):
            for j in range(1, 9):
                if board.board[i][j] == color:
                    heuristic += 1

        return heuristic

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

    # def chose_move(self):
