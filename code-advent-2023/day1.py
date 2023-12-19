import sys
from pathlib import Path

str_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def run():
    if len(sys.argv) < 2:
        filepath = Path("day1.txt")
    else:
        filepath = Path(sys.argv[1])

    with filepath.open() as f:
        lines = f.readlines()
        ints_for_line =[]
        for line in lines:
            # digits
            first_digit = len(line) + 1
            first_value = 0

            last_digit = -1
            last_value = 0
            for dig in digits:
                first_ocurrence = line.find(dig)
                if first_ocurrence != -1 and first_digit > first_ocurrence:
                    first_digit = first_ocurrence
                    first_value = digits.index(dig) + 1

            for dig in str_digits:
                first_ocurrence = line.find(dig)
                if first_ocurrence != -1 and first_digit > first_ocurrence:
                    first_digit = first_ocurrence
                    first_value = str_digits.index(dig) + 1


            for dig in digits:
                last_ocurrence = line.rfind(dig)
                if last_ocurrence!=-1 and last_digit < last_ocurrence :
                    last_digit = last_ocurrence
                    last_value = digits.index(dig) + 1

            for dig in str_digits:
                last_ocurrence = line.rfind(dig)
                if last_ocurrence!=-1 and last_digit < last_ocurrence :
                    last_digit = last_ocurrence
                    last_value = str_digits.index(dig) + 1


            #first_value = digits.index(line[first_digit]) + 1
            #last_value = digits.index(line[last_digit]) + 1

            ints_for_line.append([str(first_value), str(last_value)])
        acum = 0
        for ints in ints_for_line:
            value = int(ints[0]+ints[1])
            acum += value
        print(acum)

if __name__ == '__main__':
    run()
