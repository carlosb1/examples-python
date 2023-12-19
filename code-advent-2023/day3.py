import sys
from pathlib import Path

def is_digit(char) -> bool:
    try:
        num = int(char)
        return True
    except:
        return False

def run():
    if len(sys.argv) < 2:
        filepath = Path("day3.txt")
    else:
        filepath = Path(sys.argv[1])

    with filepath.open() as f:
        matrix = []
        lines = f.readlines()
        row = 0
        results = []
        for line in lines:
            line = line.strip()
            num_positions_to_update=[]
            digits_to_update=[]
            new_col = [-1] * len(line)
            for (col, char) in enumerate(line):
                #print(f'{char}({row},{col}))', end=None)
                if is_digit(char):
                    num_positions_to_update.append(col)
                    digits_to_update.append(char)
                elif char != '.' :
                    results.append((row, col))
                    new_col[col] = -2
                else:
                    if num_positions_to_update:
                        for position in num_positions_to_update:
                            new_col[position] = int(''.join(digits_to_update))
                        num_positions_to_update=[]
                        digits_to_update=[]
                        #we must put the number in the positions
            matrix.append(new_col)
            row+=1
        # display
        [print(f'{row}') for row in matrix]

    cols = len(matrix[0]) -1
    rows = len(matrix) - 1

    results = []
    for (num_row, row) in enumerate(matrix):
        is_found_adj = False
        for (num_col, pos) in enumerate(row):
            #we found a digit that it is adjacent, keep searching 
            if is_found_adj and pos >=0:
                continue
            #we found a digit but now we restart for a new one
            if pos ==-1 or pos ==-2:
                is_found_adj = False
                continue

            #third situation, we have a numbrer and we need to check if it is adja.
            # check adjacents
            range_rows = [max(0, num_row -1), min(rows -1, num_row +1 ), num_row]
            range_cols = [max(0,num_col - 1), min(cols -1, num_col+1), num_col]
            for matrix_row in range_rows:
                if is_found_adj: break
                for matrix_col in range_cols:
                    if matrix[matrix_row][matrix_col] == -2:
                        is_found_adj = True
                        results.append(matrix[num_row][num_col])
                        break
    print(len(results))
    print(sum(results))

if __name__ == '__main__':
    run()
