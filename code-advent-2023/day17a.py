from dataclasses import dataclass
from collections import namedtuple
import sys
import pathlib
import heapq

Position = namedtuple('Position', ['row', 'col'])

@dataclass
class Matrix:
    _rows: int
    _cols: int
    matrix: list
    @staticmethod
    def from_content(content):
        matrix =[[ int(num) for num in  line.strip()] for line in content]
        rows = len(matrix)
        cols = len(matrix[0])
        return Matrix(rows, cols, matrix)
    def __str__(self):
        result = ""
        header_row = list(range(0,self._cols))
        result += f" {header_row}\n"
        for index, row in enumerate(self.matrix):
            result+= f'{index}{row}\n'
        result+= "@@@@"
        return result

    def is_correct_position(self, position):
        if position.row < 0 or position.row >= self._rows:
            return False
        if position.col < 0 or position.col >= self._cols:
            return False
        return True
    @staticmethod
    def from_file( path: str):
        return Matrix.from_content(pathlib.Path(path).open().readlines())

    def children(self, pos):
        positions = [
                Position(pos.row + 1, pos.col),
                Position(pos.row - 1, pos.col),
                Position(pos.row , pos.col + 1),
                Position(pos.row , pos.col - 1)
                ]
        return [ pos for pos in positions if self.is_correct_position(pos)]

    def dijkstra(self):
        distances = [
            [float('inf') for _ in range(0, self._cols)] for _ in range(0, self._rows)
        ]
        init_pos = Position(0,0)
        distances[init_pos.row][init_pos.col] = 0
        queue = [(0, init_pos)]
        while queue:
            current, pos = heapq.heappop(queue)
            #check if it was visited
            if distances[pos.row][pos.col]  < current:
                continue
            #check here other conditions
            for child in self.children(pos):
                accum_weight = self.matrix[child.row][child.col] + current
                if accum_weight < distances[child.row][child.col]:
                    distances[child.row][child.col] = accum_weight
                    heapq.heappush(queue, (accum_weight, child))
        return distances

    @staticmethod
    def calculate_path(position, parents):
        current_position = position
        path = [current_position]
        import ipdb; ipdb.set_trace()
        while current_position:
            parent = parents[current_position.row][current_position.col]
            path.append(parent)
            current_position = parent
        return path[::-1]

    def A_search_algorithm(self, target):
        distances = [
            [float('inf') for _ in range(0, self._cols)] for _ in range(0, self._rows)
        ]
        parents = [
            [ None for _ in range(0, self._cols)] for _ in range(0, self._rows)
        ]
        init_pos = Position(0,0)
        distances[init_pos.row][init_pos.col] = 0
        queue = [(0, init_pos)]
        while queue:
            weight, current = heapq.heappop(queue)
            if current == target:
                return self.calculate_path(current, parents)
            #check here other conditions
            for child in self.children(current):
                accum_weight = self.matrix[child.row][child.col] + weight
                if accum_weight < distances[child.row][child.col]:
                    distances[child.row][child.col] = accum_weight
                    heapq.heappush(queue, (accum_weight, child))
                    parents[child.row][child.col] = current

if len(sys.argv) < 2:
    str_path = "day17.txt"
else:
    str_path = sys.argv[1]

matrix = Matrix.from_file(str_path)
print(matrix)
distances = matrix.dijkstra()
print(distances)
path = matrix.A_search_algorithm(Position(12,12))
print(f'path={path}')
