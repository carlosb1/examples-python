from pathlib import Path
import sys

DEFAULT_FILE = 'day11.txt'

if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])

lines  = filepath.open().readlines()

matrix = []

positions = []

for row, line in enumerate(lines):
    cols = list(line.strip())
    matrix.append(cols)

empty_rows = []
for row, line in enumerate(matrix):
    is_clean = True
    for col, elem in enumerate(line):
            if elem =='#':
                is_clean = False
    if is_clean:
        empty_rows.append(row)

empty_cols = []
for col in range(0, len(matrix[0])):
    is_clean = True
    for row in range(0,len(matrix)):
        elem = matrix[row][col]
        if elem == '#':
            is_clean = False
    if is_clean:
        empty_cols.append(col)


for (index, row) in enumerate(empty_rows):
    matrix.insert(row + index,['%' for _ in range(0, len(matrix[0]))])

for (index, col) in enumerate(empty_cols):
    for row in range(0, len(matrix)):
        matrix[row].insert(col+index,"@")

all_indexes_to_search = []
for row, line in enumerate(matrix):
    indexes = [(row, col) for col, elem in enumerate(line) if elem == '#' ]
    all_indexes_to_search.extend(indexes)

print(all_indexes_to_search)


sum_distance = 0
for source in all_indexes_to_search:
    for target in all_indexes_to_search[all_indexes_to_search.index(source)+1:]:
            distance = abs(target[0] - source[0]) + abs(target[1] - source[1])
            sum_distance+=distance

print(sum_distance)

