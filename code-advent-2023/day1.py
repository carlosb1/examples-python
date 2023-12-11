import sys
from pathlib import Path

def be_parsed(c):
    try:
        int(c)
        return True
    except:
        return False


def run():
    if len(sys.argv) < 2:
        filepath = Path("day1.txt")
    else:
        filepath = Path(sys.argv[1])

    with filepath.open() as f:
        lines = f.readlines()
        ints_for_line =[]
        for line in lines:
            integers = [c for c in line if be_parsed(c)]
            new_value = [str(integers[0]), str(integers[-1])]
            ints_for_line.append(new_value)
        acum = 0
        for ints in ints_for_line:
            value = int(ints[0]+ints[1])
            acum += value
        print(acum)

if __name__ == '__main__':
    run()
