from pathlib import Path
import sys

DEFAULT_FILE = 'day14.txt'

def print_matrix(matrix):
    for line in matrix:
        print(line)

def move_elem(row, col, matrix):
    index_row = row
    not_move=True
    previous_row = index_row
    index_row -= 1
    while not_move and  index_row >= 0:
        current_elem = matrix[index_row][col]
        if current_elem == 'O' or current_elem == '#':
            not_move = False
        else:
            matrix[index_row][col] = 'O'
            matrix[previous_row][col] = '.'
        previous_row = index_row
        index_row -= 1



if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])

lines = filepath.open().readlines()

matrix = [list(line.strip()) for line in lines]

print_matrix(matrix)
print("///////////////////////")
for col in range(0, len(matrix[0])):
    for row in range(0, len(matrix)):
        #print(f"row={row} col={col}---------")
        if matrix[row][col] == 'O':
            move_elem(row, col, matrix)
print_matrix(matrix)

siz_rows = len(matrix)

sum_all = 0
for row in range(0, len(matrix)):
    for col in range(0, len(matrix[0])):
        if matrix[row][col] == 'O':
            sum_all += siz_rows - row

print(sum_all)
