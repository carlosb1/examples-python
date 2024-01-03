from typing import List
from dataclasses import dataclass
from collections import namedtuple
import sys
import pathlib
import heapq

Position = namedtuple('Position', ['row', 'col'])

@dataclass
class Matrix:
    _matrix: list
    _rows: int
    _cols: int
    _solutions: list
    _best_solution: list
    @staticmethod
    def from_content(content):
        matrix =[[ int(num) for num in  line.strip()] for line in content]
        rows = len(matrix)
        cols = len(matrix[0])
        return Matrix(matrix, rows, cols, [], [])
    def __str__(self):
        result = ""
        header_row = list(range(0,len(self._matrix[0])))
        result += f" {header_row}\n"
        for index, row in enumerate(self._matrix):
            result+= f'{index}{row}\n'
        result+= "@@@@"
        return result

    def draw(self, positions):
        draw_matrix = Matrix([row[:] for row in self._matrix], self._rows, self._cols, [],[])
        for pos in positions:
            draw_matrix._matrix[pos.row][pos.col] = '#'
        return draw_matrix
    def height(self, path):
        if not path:
            return float('inf')
        return sum([ self._matrix[pos.row][pos.col] for pos in path])
    def solution_height(self):
        return self.height(self._best_solution)
    @staticmethod
    def from_file( path: str):
        return Matrix.from_content(pathlib.Path(path).open().readlines())

    def add_solution(self, solution):
        if solution in self._solutions:
            return
        self._solutions.append(solution)
        if self.solution_height() > self.height(solution):
            print("/////////////")
            print(matrix.draw(path.positions))
            #print_paths(available_paths)
            print(f"path.height={matrix.height(path)}")
            self._best_solution = solution



@staticmethod
def generate_possible_new_positions(matrix, positions):
    offset = 1
    last_position = positions[-1]
    new_positions_down = positions + [Position(last_position.row + offset, last_position.col)]
    new_positions_right = positions  + [Position(last_position.row, last_position.col + offset)]
    new_positions_up = positions + [Position(last_position.row - offset, last_position.col)]
    new_positions_left =positions +  [Position(last_position.row, last_position.col - offset)]

    candidate_positions = [new_positions_down, new_positions_right, new_positions_up, new_positions_left]
    filtered_positions = [pos for pos in candidate_positions if is_good_new_positions(pos, matrix)]
    return filtered_positions

@staticmethod
def is_good_new_positions(new_positions, matrix) :
    last_added_position = new_positions[-1]
    if last_added_position.row < 0 or last_added_position.row >= matrix._rows:
            return False

    if last_added_position.col < 0 or last_added_position.col >= matrix._cols:
            return False
    # repeated
    if last_added_position in new_positions[:-1]:
        return False
    #no constraints
    if len(new_positions) <= 3:
        return True

    last_row = last_added_position.row
    last_col = last_added_position.col
    same_row = all([ last_row == pos.row for pos in new_positions[-4:]])
    same_col = all([ last_col == pos.col for pos in new_positions[-4:]])
    if same_col or same_row:
        return False

    return True

def print_paths(paths):
    for path in paths:
        print(f'- {path}')


if len(sys.argv) < 2:
    str_path = "day17.txt"
else:
    str_path = sys.argv[1]

matrix = Matrix.from_file(str_path)
print(matrix)


position = Position(row=0, col=0)
final_position = Position(row=matrix._rows - 1, col=matrix._cols - 1)

available_paths = []
initial_path = [position]
heapq.heappush(available_paths, (matrix.height(initial_path), initial_path))

visited = []
while available_paths:
    (new_height, path) = heapq.heappop(available_paths)
    last_position = path[-1]
    if  last_position == final_position:
        matrix.add_solution(path)
    else:
        #if path keep being a smaller heat that the current solution, if not, discard the solution_height
        if matrix.solution_height() > new_height and path not in visited:
            visited.append(path)
            print(matrix.draw(path))
            print("/////////////")
            for new_path in generate_possible_new_positions(matrix, path):
                heapq.heappush(available_paths, (matrix.height(new_path), new_path))
    #print(matrix)
    #print("/////////////")
    # print(matrix.draw(path))
    #print_paths(available_paths)
    # input()
