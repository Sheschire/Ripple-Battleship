from django.test import TestCase
from game.views import is_collision_or_touch, _is_adjacent_position_occupied

class ShipPositionTestCase(TestCase):
    """Test ship placement on board"""
    def test_grid_creation(self):
        """Test grid creation"""
        grid_size = 5
        board = [[0 for x in range(grid_size)] for y in range(grid_size)]
        self.assertEqual(board, [
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], 
        ])
    
    def test_is_adjacent_position_occupied(self):
        """Test all position around"""
        grid_size = 5
        board = [[0 for x in range(grid_size)] for y in range(grid_size)]
        board[0][0] = 1
        self.assertEqual(_is_adjacent_position_occupied(board, 1, 0,grid_size), True)
        self.assertEqual(_is_adjacent_position_occupied(board, 1, 1,grid_size), True)
        self.assertEqual(_is_adjacent_position_occupied(board, 0, 0,grid_size), True)
        self.assertEqual(_is_adjacent_position_occupied(board, 2, 0,grid_size), False)

    def test_is_collision_or_touch(self):
        """Test each point of a ship"""
        grid_size = 5
        board  = [[0 for x in range(grid_size)] for y in range(grid_size)]

        # With horizontal orientation
        board[0][3] = 1
        board[0][4] = 1
        ship_size = 3
        orientation = 'horizontal'
        x = 0
        y = 0
        # Touching by right side
        self.assertEqual(is_collision_or_touch(
            board, ship_size, orientation, x, y, grid_size
        ), True)
        # Touching in diagonals
        self.assertEqual(is_collision_or_touch(
            board, ship_size, orientation, x + 1, y, grid_size
        ), True)
        # Not touching
        self.assertEqual(is_collision_or_touch(
            board, ship_size, orientation, x + 2, y, grid_size
        ), False)

        # With horizontal orientation
        board[0][3] = 0
        board[0][4] = 0
        board[3][1] = 1
        board[4][1] = 1
        ship_size = 3
        orientation = 'vertical'
        x = 0
        y = 1
        # Touching by bottom side
        self.assertEqual(is_collision_or_touch(
            board, ship_size, orientation, x, y, grid_size
        ), True)
        # Touching in diagonals
        self.assertEqual(is_collision_or_touch(
            board, ship_size, orientation, x, y + 1, grid_size
        ), True)
        # Not touching
        self.assertEqual(is_collision_or_touch(
            board, ship_size, orientation, x, y + 2, grid_size
        ), False)

