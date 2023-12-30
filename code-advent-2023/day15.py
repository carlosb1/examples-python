from pathlib import Path
import sys

DEFAULT_FILE = 'day15.txt'

if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])

content = filepath.open().readlines()[0][:-1]

sum_all = 0
for code in content.split(","):
    current_value = 0
    for c in code:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    print(f'{current_value}')
    sum_all += current_value
print(sum_all)
