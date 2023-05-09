from django.shortcuts import render
import random


def _is_adjacent_position_occupied(board, x, y, grid_size):
        """Check adjacent positions"""
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x+i) >= 0 and (x+i) < grid_size and (y+j) >= 0 and (y+j) < grid_size:
                    if board[x+i][y+j] != 0:
                        return True
        return False

def is_collision_or_touch(board, ship_size, orientation, x, y, grid_size):
    """Check for collision on the position or adjacent"""
    for i in range(ship_size):
        if orientation == 'horizontal' and _is_adjacent_position_occupied(board, x, y + i, grid_size):
            return True
        elif orientation == 'vertical' and _is_adjacent_position_occupied(board, x + i, y, grid_size):
            return True
    return False


def fill_with_ships(board, ships, grid_size):
    """Fill board with ships after finding placement"""
    for ship, ship_size in ships:
        ship_well_placed = False
        while ship_well_placed is False:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x = random.randint(0, grid_size - 1)
                y = random.randint(0, grid_size - ship_size)
            elif orientation == 'vertical':
                x = random.randint(0, grid_size - ship_size)
                y = random.randint(0, grid_size - 1)
            if not is_collision_or_touch(board, ship_size, orientation, x, y, grid_size):
                for i in range(ship_size):
                    if orientation == 'horizontal':
                        board[x][y + i] = ship
                    else:
                        board[x + i][y] = ship
                ship_well_placed = True


def start_game(request):
    """Receive grid_size and init board"""
    grid_size = int(request.POST.get('grid_size'))
    board = [[0 for x in range(grid_size)] for y in range(grid_size)]
    ships = [('Croiseur', 4), ('Escorteurs', 3), ('Escorteurs', 3), ('Torpilleurs', 2), 
            ('Torpilleurs', 2), ('Torpilleurs', 2), ('Sous-marins', 1), 
            ('Sous-marins', 1), ('Sous-marins', 1), ('Sous-marins', 1)]
    fill_with_ships(board, ships, grid_size)
    return render(request, "game.html", {
        'board': board,
    })


def index(request):
    """Index"""
    return render(request, "index.html")
