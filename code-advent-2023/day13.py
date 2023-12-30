from pathlib import Path
import sys

DEFAULT_FILE = 'day13.txt'

if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])

lines = filepath.open().readlines()

patterns = []
current_pattern=[]
for line in lines:
    line = line.strip()
    if len(line) == 0:
        patterns.append(current_pattern)
        current_pattern=[]
    if len(line) != 0:
        current_pattern.append(list(line.strip()))

patterns.append(current_pattern)


def find_better_reflection_rows( pattern):
    siz_rows = len(pattern)
    siz_cols = len(pattern[0])
    good_result = -1
    row = 0
    while row < siz_rows:
        inverse_index_row = row
        index_row = row + 1
        is_found = False
        while inverse_index_row >= 0 and index_row < siz_rows and not is_found:
            for index_col in range(0, siz_cols, 1):
                if pattern[index_row][index_col] != pattern[inverse_index_row][index_col]:
                    is_found = True
                    break
            inverse_index_row -= 1
            index_row += 1
        if not is_found and row != (siz_rows - 1):
            good_result = row
            break
        row+=1
    return good_result

def find_better_reflection_cols(pattern):
    siz_rows = len(pattern)
    siz_cols = len(pattern[0])
    good_result = -1
    col = 0
    while col < siz_cols:
        inverse_index_col = col
        index_col = col + 1
        is_found = False
        while inverse_index_col >= 0 and index_col < siz_cols and not is_found:
            for index_row in range(0, siz_rows, 1):
                if pattern[index_row][index_col] != pattern[index_row][inverse_index_col]:
                    is_found=True
                    break
            inverse_index_col -= 1
            index_col += 1

        if not is_found and col != (siz_cols - 1):
            good_result = col
            break
        col+=1

    return good_result

def print_matrix(pattern):
    for line in pattern:
        print(line)

all_sums = []
for indx, patterns in enumerate(patterns):
    col = find_better_reflection_cols(patterns)
    print(f'indx={indx} after={col}')
    print_matrix(patterns)
    print("///////////////")

    #print(f'indx={indx} before={rows} after={find_rows}')
    row = find_better_reflection_rows(patterns)
    print(f'indx={indx} after={row}')
    print_matrix(patterns)
    print("///////////////")
    all_sums.append((col  + 1) + ((row + 1) * 100))




print(sum(all_sums))
