# -*- coding: utf-8 -*-
import unittest
from collections import namedtuple

from mock import patch, Mock, call as mock_call

from models import minimax_alfabeta

from models import move

class TestMiniMax(unittest.TestCase):


    def setUp(self):
        self._make_boards_mocks()

    def tearDown(self):
        pass

    def test_should_call_heuristic_value_if_depth_0(self):
        depth = 0
        heuristic_function = lambda board, color: 'value'
        mini_max = minimax_alfabeta.MiniMaxAlfaBeta()

        result = mini_max.mini_max_alfa_beta(
            'board',
            depth,
            'color',
            'parent_alfa',
            'parent_beta',
            'max_gamer',
            heuristic_function
        )
        expected_result = 'value'
        self.assertEqual(expected_result, result)

    def _make_board_mock(self, name, clones, valid_moves):
        board = Mock()
        board.board_name = name
        board._opponent = Mock(return_value='color')
        board.play = Mock()
        if clones:
            board.get_clone = Mock(side_effect=clones)
        if valid_moves:
            board.valid_moves = Mock(return_value=valid_moves)
        return board

    def _make_boards_mocks(self):
        self.leaf_boards = []
        for i in xrange(0, 8):
            self.leaf_boards.append(
                self._make_board_mock('leaf%d'%i, None, None)
            )

        self.board_1_1 = self._make_board_mock(
            'self.board_1_1',
            [
                self.leaf_boards[0],
                self.leaf_boards[1],
            ],
            ['move1', 'move2']
        )
        self.board_1_2 = self._make_board_mock(
            'self.board_1_2',
            [
                self.leaf_boards[2],
                self.leaf_boards[3], # não pode ser chamado
            ],
            ['move3', 'move4'] # nao chama o move4
        )

        self.board_1_3 = self._make_board_mock(
            'self.board_1_3',
            [
                self.leaf_boards[4],
                self.leaf_boards[5],
            ],
            ['move5', 'move6']
        )

        self.board_1_4 = self._make_board_mock(
            'self.board_1_4',
            [
                self.leaf_boards[6],
                self.leaf_boards[7],
            ],
            ['move7', 'move8']
        )

        self.board_2_1 = self._make_board_mock(
            'self.board_2_1',
            [
                self.board_1_1,
                self.board_1_2,
            ],
            ['move9', 'move10']
        )

        self.board_2_2 = self._make_board_mock(
            'self.board_2_2',
            [
                self.board_1_3,
                self.board_1_4,
            ],
            ['move11', 'move12']
        )

        self.board_3 = self._make_board_mock(
            'self.board_3',
            [
                self.board_2_1,
                self.board_2_2,
            ],
            ['move13', 'move14']
        )


    # @patch('models.minimax_alfabeta.Move', Mock())
    # def test_simples(self):
    #     leaf_boards = []
    #     for i in xrange(0, 8):
    #         leaf_boards.append(
    #             self._make_board_mock('leaf%d'%i, None, None)
    #         )

    #     board_1_1 = self._make_board_mock(
    #         'board_1_1',
    #         [
    #             leaf_boards[0],
    #             leaf_boards[1],
    #         ],
    #         ['move1', 'move2']
    #     )
    #     board_1_2 = self._make_board_mock(
    #         'board_1_2',
    #         [
    #             leaf_boards[2],
    #             leaf_boards[3], # não pode ser chamado
    #         ],
    #         ['move3', 'move4'] # nao chama o move4
    #     )

    #     board_1_3 = self._make_board_mock(
    #         'board_1_3',
    #         [
    #             leaf_boards[4],
    #             leaf_boards[5],
    #         ],
    #         ['move5', 'move6']
    #     )

    #     board_1_4 = self._make_board_mock(
    #         'board_1_4',
    #         [
    #             leaf_boards[6],
    #             leaf_boards[7],
    #         ],
    #         ['move7', 'move8']
    #     )

    #     board_2_1 = self._make_board_mock(
    #         'board_2_1',
    #         [
    #             board_1_1,
    #             board_1_2,
    #         ],
    #         ['move9', 'move10']
    #     )

    #     board_2_2 = self._make_board_mock(
    #         'board_2_2',
    #         [
    #             board_1_3,
    #             board_1_4,
    #         ],
    #         ['move11', 'move12']
    #     )

    #     board_3 = self._make_board_mock(
    #         'board_3',
    #         [
    #             board_2_1,
    #             board_2_2,
    #         ],
    #         ['move13', 'move14']
    #     )


    #     heuristic_values = [12, 5, 25, 3, 5, 10, 1, 2]
    #     heuristic_function = Mock(side_effect=heuristic_values)

    #     depth = 3

    #     mini_max = minimax_alfabeta.MiniMaxAlfaBeta()

    #     best_value = mini_max.mini_max_alfa_beta(
    #         board_3,
    #         depth,
    #         'color',
    #         float('-inf'),
    #         float('inf'),
    #         True,
    #         heuristic_function
    #     )
    #     expected_best_value = 12
    #     self.assertEqual(expected_best_value, best_value)



    @patch('models.minimax_alfabeta.Move', Mock())
    def test_best_value_with_board_1_1_is_correct(self):

        heuristic_values = [12, 5]
        heuristic_function = Mock(side_effect=heuristic_values)

        depth = 1

        mini_max = minimax_alfabeta.MiniMaxAlfaBeta()

        best_value = mini_max.mini_max_alfa_beta(
            self.board_1_1,
            depth,
            'color',
            float('-inf'),
            float('inf'),
            True,
            heuristic_function
        )
        expected_best_value = 12
        self.assertEqual(expected_best_value, best_value)



    @patch('models.minimax_alfabeta.Move', Mock())
    def test_best_value_with_board_1_1_is_correct_with_heuristic_value_exchanged(self):

        heuristic_values = [5, 12]
        heuristic_function = Mock(side_effect=heuristic_values)

        depth = 1

        mini_max = minimax_alfabeta.MiniMaxAlfaBeta()

        best_value = mini_max.mini_max_alfa_beta(
            self.board_1_1,
            depth,
            'color',
            float('-inf'),
            float('inf'),
            True,
            heuristic_function
        )
        expected_best_value = 12
        self.assertEqual(expected_best_value, best_value)

    @patch('models.minimax_alfabeta.Move', Mock())
    def test_best_value_with_board_3_is_correct(self):

        heuristic_values =  [12, 5, 25, 3, 5, 10, 1, 2]
        heuristic_function = Mock(side_effect=heuristic_values)

        depth = 3

        mini_max = minimax_alfabeta.MiniMaxAlfaBeta()

        best_value = mini_max.mini_max_alfa_beta(
            self.board_3,
            depth,
            'color',
            float('-inf'),
            float('inf'),
            True,
            heuristic_function
        )
        expected_best_value = 12
        self.assertEqual(expected_best_value, best_value)

    @patch('models.minimax_alfabeta.Move', Mock())
    def test_best_value_with_board_3_is_correct_and_is_pruning(self):

        heuristic_values =  [12, 5, 25, 5, 10]
        heuristic_function = Mock(side_effect=heuristic_values)

        depth = 3

        mini_max = minimax_alfabeta.MiniMaxAlfaBeta()

        best_value = mini_max.mini_max_alfa_beta(
            self.board_3,
            depth,
            'color',
            float('-inf'),
            float('inf'),
            True,
            heuristic_function
        )
        expected_best_value = 12
        self.assertEqual(expected_best_value, best_value)

    @patch('models.minimax_alfabeta.Move', Mock())
    def test_heuristic_function_is_called_in_right_order(self):

        heuristic_values =  [12, 5, 25, 5, 10]
        heuristic_function = Mock(side_effect=heuristic_values)

        depth = 3

        mini_max = minimax_alfabeta.MiniMaxAlfaBeta()

        best_value = mini_max.mini_max_alfa_beta(
            self.board_3,
            depth,
            'color',
            float('-inf'),
            float('inf'),
            True,
            heuristic_function
        )
        calls_list = [
            mock_call(self.leaf_boards[0], 'color'),
            mock_call(self.leaf_boards[1], 'color'),
            mock_call(self.leaf_boards[2], 'color'),
            mock_call(self.leaf_boards[4], 'color'),
            mock_call(self.leaf_boards[5], 'color'),
        ]
        heuristic_function.assert_has_calls(calls_list, any_order=False)
