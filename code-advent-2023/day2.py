from pathlib import Path
import sys

available_cubes = {'red' : 12, 'green': 13, 'blue': 14}

def validate_cubes(cubes):
    return all([available_cubes[cube] >= num for (num, cube) in cubes])
def mul(values):
    elem = 1
    for value in values:
        elem *= value
    return elem

def run():
    if len(sys.argv) < 2:
        filepath = Path("day2.txt")
    else:
        filepath = Path(sys.argv[1])

    with filepath.open() as f:
        lines = f.readlines()
        adding_up = 0
        #good_games = []
        for (num, line) in enumerate(lines):
            is_good = True
            game = line.split(":")[1][:-1]
            sets = game.split(';')
            max_values = {}
            for set_ in sets:
                cubes = [(int(same_cubes.split(' ')[1]), same_cubes.split(' ')[2]) for same_cubes in set_.split(',')]
                for cube in cubes:
                    name_cube = cube[1]
                    value_cube = cube[0]
                    if name_cube not in max_values or max_values[name_cube] < value_cube :
                        max_values[name_cube] = value_cube
            adding_up += mul(max_values.values())
                # part 1
                # is_good = validate_cubes(cubes)
                # if not is_good:
                #     break
            # part 1
            #if is_good:
            #    id_ = num + 1
            #    good_games.append(id_)

    #print(sum(good_games))
    print(adding_up)


if __name__ == '__main__':
    run()
