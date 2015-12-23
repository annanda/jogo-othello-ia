import unittest
from models.players.heuristic_1_player import Heuristic1Player, heuristic_value
from models.board import Board

class TestHeuristic1(unittest.TestCase):

    def test_inicial_board(self):
        board_exemple = None
        board = Board(board_exemple)
        expected = 2
        heuristic = Heuristic1Player(board.BLACK)
        value = heuristic_value(board, board.BLACK)
        self.assertEqual(expected, value)


    def test_4_blacks(self):
        board_exemple = []

        for i in range(0, 10):
            board_exemple.insert(i, ['?']*10)

        for i in range(1, 9):
            for j in range(1, 9):
                board_exemple[i][j] = '.'

        board_exemple[4][4], board_exemple[4][5] = 'o', '@'
        board_exemple[5][4], board_exemple[5][5] = '@', 'o'
        board_exemple[6][6], board_exemple[7][7] = '@', '@'

        board = Board(board_exemple)
        expected = 4
        heuristic = Heuristic1Player(board.BLACK)
        value = heuristic_value(board, board.BLACK)
        self.assertEqual(expected, value)


    def test_8_whites(self):
        board_exemple = []

        for i in range(0, 10):
            board_exemple.insert(i, ['?']*10)

        for i in range(1, 9):
            for j in range(1, 9):
                board_exemple[i][j] = '.'

        board_exemple[4][4], board_exemple[4][5] = 'o', '@'
        board_exemple[5][4], board_exemple[5][5] = '@', 'o'
        board_exemple[6][6], board_exemple[7][7] = '@', '@'

        board_exemple[1][4], board_exemple[5][7] = 'o', 'o'
        board_exemple[2][4], board_exemple[8][1] = 'o', 'o'
        board_exemple[3][6], board_exemple[8][2] = 'o', 'o'


        board = Board(board_exemple)
        expected = 8
        heuristic = Heuristic1Player(board.WHITE)
        value = heuristic_value(board, board.WHITE)
        self.assertEqual(expected, value)