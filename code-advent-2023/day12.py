from pathlib import Path
import sys

DEFAULT_FILE = 'day12.txt'

if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])

def find_ranges(line: str):
    ranges = []
    in_range = False
    new_range = 0
    for c in line:
        if c == '#' and not in_range:
            # save previous
            if new_range > 0:
                ranges.append(new_range)
            # reset for the new one
            in_range = True
            new_range = 0
        if c == '#' and in_range:
            new_range +=1
        if c != '#':
            in_range= False
    if new_range > 0:
        ranges.append(new_range)
    return ranges

def end_threshold(input_arry, index_to_change):
    #check if it is all checked
    if len(input_arry) == index_to_change:
        return True
    #it should not be necessary
    if "?" not in input_arry:
        return True
    return False
def add_input_array(type_combination, input_arry, index_to_start):
    input_arry = list(input_arry)
    index = input_arry.index('?', index_to_start)
    input_arry[index] = type_combination
    return ''.join(input_arry)

def is_solution(input_arry, expected_damages):
    if '?' in input_arry:
        return False
    sort_found_ranges = find_ranges(input_arry)
    return sort_found_ranges == expected_damages

def generate_combination(input_arry, index_to_change, ret_val, expected_damages):
    if is_solution(input_arry, expected_damages):
        ret_val.append(input_arry)

    if end_threshold(input_arry, index_to_change):
        return
    try:
        #if it is an error
        new_comb = add_input_array('#', input_arry, index_to_change)
        #print(f'{new_comb} index={index_to_change}')
        #if it is the last one
        try:
            index = input_arry.index('?', index_to_change + 1)
        except:
            index = len(input_arry)
        generate_combination(new_comb, index, ret_val, expected_damages)
    except:
        print('Not possible add combination')

    try:
        #if it is an error
        new_comb = add_input_array('.', input_arry, index_to_change)
        #print(f'{new_comb} index={index_to_change}')
        #if it is the last one
        try:
            index = input_arry.index('?', index_to_change + 1)
        except:
            index = len(input_arry)
        generate_combination(new_comb, index, ret_val, expected_damages)
    except:
        print('Not possible add combination')


lines = [line.strip() for line in filepath.open().readlines()]

all_sums = []
for line in lines:
    ret_val = []
    combination = line.split(' ')[0]
    expected_damages = [int(val) for val in line.split(' ')[1].split(',')]
    print(f'combination={combination}')
    generate_combination(combination, 0, ret_val, expected_damages)
    #print(f'expected={expected_damages}')
    #print(ret_val)
    all_sums.append(len(ret_val))

print(sum(all_sums))

#print("--------------")
#print(total_damages)



