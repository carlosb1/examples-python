from pathlib import Path
from enum import Enum
import sys
class UserMove(Enum):
    North = 1,
    South = 2,
    East=3,
    West=4
    def move(self, pos):
        if self == UserMove.North:
            return (pos[0]-1, pos[1])
        elif self == UserMove.South:
            return (pos[0]+1, pos[1])
        elif self == UserMove.East:
            return (pos[0], pos[1]+1)
        elif self == UserMove.West:
            return (pos[0], pos[1]-1)
        else:
            return pos

class Pipe(Enum):
    NorthSouth = [UserMove.North, UserMove.South],
    EastWest = [UserMove.East, UserMove.West],
    NorthEast = [UserMove.North, UserMove.East],
    NorthWest = [UserMove.North, UserMove.West],
    SouthWest = [UserMove.South, UserMove.West],
    SouthEast  = [UserMove.South, UserMove.East],
    Initial  = [UserMove.South, UserMove.East, UserMove.West, UserMove.East],
    NonePipe    = []

DEFAULT_FILE = 'day10.txt'

if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])

lines  = filepath.open().readlines()

for line in lines:
    print(line.strip())

cols = len(lines[0])

maze = [[[]]*cols for _ in range(0, len(lines))]
counts = [[-1]*cols for _ in range(0, len(lines))]
init_posic = []
for (row, line) in enumerate(lines):
    for (col, pos) in enumerate(line):
        if pos == '|':
            maze[row][col] = Pipe.NorthSouth.value[0]
        elif pos == '-':
            maze[row][col] = Pipe.EastWest.value[0]
        elif pos == 'L':
            maze[row][col] = Pipe.NorthEast.value[0]
            pass
        elif pos == 'J':
            maze[row][col] = Pipe.NorthWest.value[0]
            pass
        elif pos == '7':
            maze[row][col] = Pipe.SouthWest.value[0]
            pass
        elif pos == 'F':
            maze[row][col] = Pipe.SouthEast.value[0]
            pass
        elif pos == 'S':
            maze[row][col] = Pipe.Initial.value[0]
            counts[row][col] = 0
            init_posic = [row, col]
        else:
            pass

def opposite(pipe):
    if pipe == UserMove.East:
        return UserMove.West
    elif pipe == UserMove.North:
        return UserMove.South
    elif pipe == UserMove.West:
        return UserMove.East
    else:
        return UserMove.North


def good_movements(maze, moves, current_posic):
    rows = len(maze)
    cols = len(maze[1])
    good_moves = []

    for move in moves:
        posic = move.move(current_posic)
        #limits
        if posic[0] < 0 and posic[0] >= rows and posic[1] >= cols:
            continue
        #None pipe
        if maze[posic[0]][posic[1]] == Pipe.NonePipe:
            continue
        pipe = maze[posic[0]][posic[1]]
        move  = opposite(move)# find expected pipe
        if move in pipe:
            list_pipe = list(pipe)
            list_pipe.remove(move)
            good_moves.append((posic,list_pipe[0]))
    return good_moves

for line in maze:
    print(line)

all_posics = []
all_posics.append(good_movements(maze, Pipe.Initial.value[0], init_posic))

for line in maze:
    print(line)


top_number = 0

dist = 0
while len(all_posics) != 0:
    dist +=1
    posics = all_posics[0]
    del all_posics[0]
    new_posics = []
    while posics:
        struc_move = posics.pop()
        posic = struc_move[0]
        #dicard if it was counted
        if counts[posic[0]][posic[1]] != -1:
            continue
        if top_number < dist:
            top_number = dist
        counts[posic[0]][posic[1]] = dist
        new_posics.extend(good_movements(maze,[struc_move[1]],posic))
    #add if list is not empty
    if new_posics:
        all_posics.append(new_posics)

for line in lines:
    print(line.strip())

for count in counts:
    print(count)

print(top_number)


#print(maze)

