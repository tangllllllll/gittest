'''docstring'''
import unittest
from itertools import chain
from itertools import cycle
from unittest import TestCase
from unittest.mock import patch, Mock, call

from game_map import GameMap

__name__ == '__tll__'



class TestGameMap(TestCase):

    def setUp(self):
        self.game_map = GameMap(4, 3)

    def test_rows(self):
        self.assertEqual(4, self.game_map.rows, "Should get correct rows")

    def test_cols(self):
        self.assertEqual(3, self.game_map.cols, "Should get correct cols")

    @patch('random.random', new=Mock(side_effect=chain(cycle([0.3, 0.6, 0.9]))))
    def test_reset(self):
        self.game_map.reset()
        for i in range(0, 4):
            self.assertEqual(1, self.game_map.get(i, 0))
            for j in range(1, 3):
                self.assertEqual(0, self.game_map.get(i, j))

    def test_get_set(self):
        self.assertEqual(0, self.game_map.get(0, 0), "Cells init to zero")
        self.game_map.set(0, 0, 1)
        self.assertEqual(1, self.game_map.get(0, 0), "Should get value set by set")

    def test_get_neighbor_count(self):
        expected_value = [[8] * 3] * 4
        self.game_map.cells = [[1] * 3] * 4
        for i in range(0, 4):
            for j in range(0, 3):
                x = self.game_map.get_neighbor_count(i, j)
                self.assertEqual(expected_value[i][j], x, '(%d,%d)' % (i, j))

    @patch('game_map.GameMap.get_neighbor_count', new=Mock(return_value=8))
    def test_get_neighbor_count_map(self):
        expected_value = [[8] * 3] * 4
        self.assertEqual(expected_value, self.game_map.get_neighbor_count_map())

    def test_set_map(self):
        self.assertRaises(TypeError, self.game_map.set_map, {(0, 0): 1})
        self.assertRaises(AssertionError, self.game_map.set_map, [[1] * 3] * 3)
        self.assertRaises(TypeError, self.game_map.set_map, [['1'] * 3] * 4)
        self.assertRaises(AssertionError, self.game_map.set_map, [[2] * 3] * 4)

        self.game_map.set_map([[1] * 3] * 4)
        self.assertEqual([[1] * 3] * 4, self.game_map.cells)

    def test_print_map(self):
        self.game_map.cells = [
            [0, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        with patch('builtins.print')as mock:
            self.game_map.print_map()
            mock.assert_has_calls(
                [
                    call('0 1 1'),
                    call('0 0 1'),
                    call('1 1 1'),
                    call('0 0 0'),
                ]
            )
        self.game_map.cells = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        with patch('builtins.print')as mock:
            self.game_map.print_map()
            mock.assert_has_calls(
                [
                    call('1 1 1'),
                    call('1 1 1'),
                    call('1 1 1'),
                    call('1 1 1'),
                ]
            )


if __name__ == '__main__':
     unittest.main()
