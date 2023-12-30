from pathlib import Path
from dataclasses import dataclass
from typing import Tuple, Optional
from enum import Enum
import sys

Direction = Enum('Direction', ['LEFT', 'RIGHT', 'UP', 'DOWN'])

@dataclass
class Walker:
    pos: Tuple[int, int]
    direction: Direction
    rows: int
    cols: int

    def move(self,energized) -> Optional[Tuple[int, int]]:
        pos = self.pos
        if draw_matrix[pos[0]][pos[1]] == '.':
            draw_matrix[pos[0]][pos[1]] = '#'
        energized.append(pos)
        if self.direction == Direction.DOWN:
            if self.pos[0] + 1 >= rows:
                return None
            pos = (self.pos[0] + 1, self.pos[1])
        elif self.direction == Direction.UP:
            if self.pos[0] - 1 < 0:
                return None
            pos = (self.pos[0] - 1, self.pos[1])
        elif self.direction == Direction.RIGHT:
            if self.pos[1] + 1 >= cols:
                return None
            pos = (self.pos[0], self.pos[1] + 1 )
        elif self.direction == Direction.LEFT:
            if self.pos[1] - 1 < 0:
                return None
            pos = (self.pos[0], self.pos[1] - 1)
        self.pos = pos
        return pos

DEFAULT_FILE = 'day16.txt'

def print_matrix(matrix):
    header_row = list(range(0,len(matrix[0])))
    str_row = [f'{num}' for num in header_row]
    print(f" {str_row}")
    for index, row in enumerate(matrix):
        print(f'{index}{row}')
    print("@@@@")

def size(matrix) -> Tuple[int, int]:
    rows = len(matrix)
    cols = len(matrix[0])
    return (rows, cols)


if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])

matrix =[list(line.strip()) for line in filepath.open().readlines()]
draw_matrix =[list(line.strip()) for line in filepath.open().readlines()]

print_matrix(matrix)
(rows, cols) = size(matrix)

init_pos = (0,0)
direction = Direction.RIGHT

available_walkers = []

energized = []

def is_clean_road(tile: str):
    return tile == '.'

#TODO check first case
available_walkers.append(Walker(init_pos, direction, rows, cols))

while available_walkers:
    [print(f'pending_walkers={walker}') for walker in available_walkers]
    road = available_walkers.pop()
    current_pos = road.pos
    current_place = matrix[current_pos[0]][current_pos[1]]
    while is_clean_road(current_place):
        current_pos = road.move(energized)
        if current_pos  is None:
            break
        print(f'{current_pos}')
        current_place = matrix[current_pos[0]][current_pos[1]]
        print(f"Walking to {current_pos}")
    if current_place == '|':
        if road.direction == Direction.LEFT or road.direction == Direction.RIGHT:
            walker_up = Walker(current_pos, Direction.UP, rows, cols)
            new_pos = walker_up.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker_up)
            walker_down = Walker(current_pos, Direction.DOWN, rows, cols)
            new_pos = walker_down.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker_down)
        else:
            new_pos = road.move(energized)
            if new_pos is not None:
                available_walkers.append(road)
    elif current_place == '-':
        if road.direction == Direction.UP or road.direction == Direction.DOWN:
            walker_left = Walker(current_pos, Direction.LEFT, rows, cols)
            new_pos = walker_left.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker_left)
            walker_right = Walker(current_pos, Direction.RIGHT, rows, cols)
            new_pos = walker_right.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker_right)
        else:
            new_pos = road.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(road)
    elif current_place == '\\':
        if road.direction == Direction.UP:
            walker_up = Walker(current_pos, Direction.LEFT, rows, cols)
            new_pos = walker_up.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker_up)
        elif road.direction == Direction.RIGHT:
            walker_right = Walker(current_pos, Direction.DOWN, rows, cols)
            new_pos = walker_right.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker_right)
        if road.direction == Direction.DOWN:
            walker = Walker(current_pos, Direction.RIGHT, rows, cols)
            new_pos = walker.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker)
        elif road.direction == Direction.LEFT:
            walker = Walker(current_pos, Direction.UP, rows, cols)
            new_pos = walker.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker)

    elif current_place == '/':
        if road.direction == Direction.UP:
            walker = Walker(current_pos, Direction.RIGHT, rows, cols)
            new_pos = walker.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker)
        elif road.direction == Direction.LEFT:
            walker = Walker(current_pos, Direction.DOWN, rows, cols)
            new_pos = walker.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker)
        if road.direction == Direction.DOWN:
            walker = Walker(current_pos, Direction.LEFT, rows, cols)
            new_pos = walker.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker)
        elif road.direction == Direction.RIGHT:
            walker = Walker(current_pos, Direction.UP, rows, cols)
            new_pos = walker.move(energized)
            if new_pos is not None and new_pos not in available_walkers:
                available_walkers.append(walker)

    else:
        assert "It should break, it is an incorrect character"



    print_matrix(draw_matrix)
    #time.sleep(0.5)
    input()

