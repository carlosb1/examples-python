import sys
from dataclasses import dataclass
from pathlib import Path
from parse import compile
import parse

DEFAULT_FILE = 'day8.txt'

@dataclass
class Node:
    id: str
    left: str
    right: str

if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])

p = compile("{} = ({}, {})")


lines = filepath.open().readlines()
store = {}
directions = lines[0].strip()
for line in lines[2:]:
    strip_line = line.strip()
    print(strip_line)
    parsed_line  = p.parse(strip_line)
    if type(parsed_line) != parse.Result:
        break
    parsed_line.fixed
    origin=parsed_line[0]
    left=parsed_line[1]
    right=parsed_line[2]
    store[origin] = Node(origin, left, right)


current_step = 'AAA'

index_seq=0

steps = 0
found = False
while not found:
    for (index, direct ) in enumerate(directions):
            node = store[current_step]
            print(f'step={index},direct={direct},node={node}')
            if direct == 'L':
                current_step = node.left
            elif direct == 'R':
                current_step = node.right
            else:
                assert False
            if node.id == 'ZZZ':
                found=True
                break
            steps+=1

print(steps)



