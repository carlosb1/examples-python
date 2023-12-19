import sys
from pathlib import Path

DEFAULT_FILE = 'day4.txt'

def run():
    if len(sys.argv) < 2:
        filepath = Path(DEFAULT_FILE)
    else:
        filepath = Path(sys.argv[1])

    f = filepath.open()
    lines = f.readlines()

    list_of_lists = [ [line, 1]  for line in lines]

    index = 0
    while index < len(list_of_lists):
        elem = list_of_lists[index]
        line = elem[0]
        for _ in range(0, elem[1]):
            games = line.rstrip()
            games = ' '.join(games.split())
            games = games.split('|')
            winning_game = games[0][:-1].split(":")[1].strip().split(' ')
            your_game = games[1][1:].strip().split(' ')
            hits = set(your_game).intersection(winning_game)
            range_values = range(index+1, index + 1 + len(hits))
            for new_index in range_values:
                new_elem = list_of_lists[new_index]
                new_elem[1]+=1
        index+=1
    sum_all = sum([accum for (_, accum) in list_of_lists])
    print(sum_all)




if __name__ == '__main__':
    run()


