from typing import Tuple


#check decorators
#NAMED TUPLE

class Chessboard:
    def __init__(self, size):
        self._rows  = size
        self._cols = size

def _generate_all_possible_movements(size: int):
    return [(first_index, second_index) for first_index in range(0,size)  for second_index in range(0, size)]

def remove(pieces, movement: Tuple):
    pieces.remove(movement)

def display(chessboard, pieces):
    pieces = sorted(pieces)
    print(str(pieces))
    print("\n", end="")
    for current_row in range(0,chessboard._rows):
        for current_col in range(0,chessboard._cols):
            if (chessboard._rows - current_row - 1, current_col) in pieces:
                print("[X]", end="")
            else:
                print("[ ]",end="")
        print("\n", end="")


def jump(chessboard, current_movement, history_movements, iteration=0):
    if current_movement in history_movements:
        assert "It could not be append, it exists"
    new_history = history_movements.copy()
    new_history.append(current_movement)
    if is_finish(chessboard, new_history):
        return new_history
    # Figure out possible movements
    available_movements = possible_movements(chessboard, current_movement)
    # Filter already visited
    not_visited_movements = [ movement for movement in available_movements if movement not in history_movements]
    for available_movement in not_visited_movements:
        result_history_movements = jump(chessboard, available_movement,new_history,iteration=iteration+1)
        if is_finish(chessboard, result_history_movements):
            return result_history_movements
    #If it was not possible to found a result, leave
    return history_movements

def is_finish(chessboard, pieces):
    all_possibles = (chessboard._rows * chessboard._cols)
    return len(pieces) == all_possibles and len(pieces) == len(set(pieces))

#Add typing
def possible_movements(chessboard, current_position: Tuple) :
    possible_jumps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    all_possibles_movements = [(current_position[0] + jump[0], current_position[1] + jump[1]) for jump in possible_jumps]
    correct_movements = [movement for movement in all_possibles_movements if movement[0] >= 0
                         and movement[1] >= 0 and movement[0] < chessboard._rows and movement[1] < chessboard._cols]
    return correct_movements

def test_possible_moviments():
    chessboard = Chessboard(4)
    expected_values = sorted([(3, 2), (3, 0), (2, 3), (0, 3)])
    assert expected_values == sorted(possible_movements(chessboard, (1,1)))

def test_bounder_possible_movimentes():
    chessboard = Chessboard(1)
    assert [] == sorted(possible_movements(chessboard, (0,0)))

def test_is_finished():
    expected_finished = [(0, 0)]
    chessboard = Chessboard(1)
    assert is_finish(chessboard, expected_finished)

def test_one_execution_simple_solution():
    chessboard = Chessboard(5)
    all_possible_movements = _generate_all_possible_movements(5)
    expected_all_movements = all_possible_movements.copy()
    current_movement = all_possible_movements.pop()
    result_movements= jump(chessboard, current_movement, all_possible_movements)
    assert sorted(expected_all_movements) == sorted(result_movements)


def test_two_executions_solution():
    #set up result
    expected_possible_movements = _generate_all_possible_movements(3)
    chessboard = Chessboard(3)
    current_movement = (2, 2)
    history_movements = expected_possible_movements.copy()

    movements = possible_movements(chessboard, current_movement)
    # remove current position and one iteration
    remove(history_movements, current_movement)
    remove(history_movements, movements.pop())
    result_movements = jump(chessboard, current_movement, history_movements)
    display(chessboard, result_movements)
    assert sorted(expected_possible_movements) == sorted(result_movements)

def test_knight_tour():
    #set up result
    expected_possible_movements = _generate_all_possible_movements(5)
    chessboard = Chessboard(5)
    current_movement = (2, 2)
    result_movements = jump(chessboard, current_movement, history_movements=[])
    display(chessboard, result_movements)
    assert  sorted(expected_possible_movements) == sorted(result_movements)

