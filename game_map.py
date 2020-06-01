# -*- coding: utf-8 -*-
#
# @author Epsirom

import random


class GameMap(object):
    """
    The game map, contains a lot of cells.

    Each cell has a value, 0 means it is a dead/empty cell, and 1 means it is a live cell.

    Attributes:
        size:
    """

    MAX_MAP_SIZE = 100
    MAX_CELL_VALUE = 1
    DIRECTIONS = (
        (0, 1, ),
        (0, -1, ),
        (1, 0, ),
        (-1, 0, ),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    )

    def __init__(self, rows, cols):
        """Inits GameMap with row and column count."""
        if not isinstance(rows, int):
            raise TypeError("rows should be int")
        if not isinstance(cols, int):
            raise TypeError("cols should be int")
        assert 0 < rows <= self.MAX_MAP_SIZE
        assert 0 < cols <= self.MAX_MAP_SIZE
        self.size = (rows, cols, )
        self.cells = [[0 for col in range(cols)] for row in range(rows)]

    @property
    def rows(self):
        """Get row count of the map."""
        return self.size[0]

    @property
    def cols(self):
        """Get column count of the map."""
        return self.size[1]

    def reset(self, possibility=0.5):
        """Reset the map with random data."""
        if not isinstance(possibility, float):
            raise TypeError("possibility should be float")
        for row in self.cells:
            for col_num in range(self.cols):
                row[col_num] = 1 if random.random() < possibility else 0

    def get(self, row, col):
        """Get specific cell in the map."""
        if not isinstance(row, int):
            raise TypeError("row should be int")
        if not isinstance(col, int):
            raise TypeError("col should be int")
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols
        return self.cells[row][col]

    def set(self, row, col, val):
        """Set specific cell in the map."""
        if not isinstance(row, int):
            raise TypeError("row should be int")
        if not isinstance(col, int):
            raise TypeError("col should be int")
        if not isinstance(val, int):
            raise TypeError("val should be int")
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols
        assert 0 <= val <= self.MAX_CELL_VALUE
        self.cells[row][col] = val
        return self

    def get_neighbor_count(self, row, col):
        """Get count of neighbors in specific cell.

        Args:
            row: row number
            col: column number

        Returns:
            Count of live neighbor cells
        """
        if not isinstance(row, int):
            raise TypeError("row should be int")
        if not isinstance(col, int):
            raise TypeError("col should be int")
        assert 0 <= row < self.rows
        assert 0 <= col < self.cols
        count = 0
        for d in self.DIRECTIONS:
            d_row = row + d[0]
            d_col = col + d[1]
            if d_row >= self.rows:
                d_row -= self.rows
            if d_col >= self.cols:
                d_col -= self.cols
            count += self.cells[d_row][d_col]
        return count

    def get_neighbor_count_map(self):
        return [
            [self.get_neighbor_count(row, col) for col in range(self.cols)]
            for row in range(self.rows)
            ]

    def set_map(self, new_map):
        if not isinstance(new_map, list):
            raise TypeError("new_map should be list")
        assert len(new_map) == self.rows
        for row in new_map:
            if not isinstance(row, list):
                raise TypeError("rows in new_map should be list")
            assert len(row) == self.cols
            for cell in row:
                if not isinstance(cell, int):
                    raise TypeError("cells in new_map should be int")
                assert 0 <= cell <= self.MAX_CELL_VALUE
        self.cells = new_map

    def print_map(self, cell_maps=None, sep=' '):
        if not cell_maps:
            cell_maps = ['0', '1']
        if not isinstance(cell_maps, list) and not isinstance(cell_maps, dict):
            raise TypeError("cell_maps should be list or dict")
        if not isinstance(sep, str):
            raise TypeError("sep should be string")
        for row in self.cells:
            print(sep.join([cell_maps[cell] for cell in row]))
