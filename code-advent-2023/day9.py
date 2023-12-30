from pathlib import Path
import sys


DEFAULT_FILE = 'day9.txt'

if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])

lines  = filepath.open().readlines()

results = []
for line in lines:
    result = []
    seqs = []
    number_lines = [ int(digit) for digit in line.strip().split(' ')]
    seqs.append(number_lines)
    while sum(number_lines)!=0:
        difs = [number_lines[index +1] - number_lines[index] for index in range(0,len(number_lines) - 1)]
        seqs.append(difs)
        number_lines = difs
    for index_accu in reversed(range(1, len(seqs))):
        new_incr = seqs[index_accu][-1]
        seqs[index_accu - 1].append(seqs[index_accu - 1][-1] + new_incr)
    results.append(seqs[0][-1])
print(results)
print(sum(results))
