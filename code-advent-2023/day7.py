import sys
from pathlib import Path

DEFAULT_FILE = 'day7.txt'

if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])


LABELS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K','A']

def larger(compare_hand, hand):
    compare_score = sum([in_score[0] for in_score in compare_hand[1] if in_score[0] >= 100])
    hand_score =  sum([in_score[0] for in_score in hand[1] if in_score[0] >= 100])

    if compare_score < hand_score:
        return True
    elif compare_score == hand_score:

        siz_score = len(hand[1])
        for ind_score in range(0, siz_score):
            compare_label = compare_hand[1][ind_score][1]
            label = hand[1][ind_score][1]
            if label != compare_label:
                return  LABELS.index(compare_label) < LABELS.index(label)

    return False


def append(hands, hand, bid):
        in_score = []
        for (index,label) in enumerate(LABELS):
            same_label = hand.count(label)
            if same_label == 5:
                in_score.append([100000, label])
            if same_label == 4:
                in_score.append([10000, label])
            if same_label == 3:
                in_score.append([1000, label])
            if same_label ==2:
                in_score.append([100, label])
            if same_label ==1:
                in_score.append([LABELS.index(label), label])
        in_score = sorted(in_score, key=lambda x: x[0])
        in_score.reverse()
        scored_hand = [hand, in_score , bid]
        index=0
        while index < len(hands):
            compare_hand = hands[index]
            if larger(compare_hand, scored_hand):
                break
            index+=1
        hands.insert(index, scored_hand)


hands = []
for line in filepath.open().readlines():
    parsed_line = line.strip().split(' ')
    append(hands, parsed_line[0], int(parsed_line[1]))
print(hands)

scores = 0
top_score = len(hands)
for (ind,hand) in enumerate(hands):
    bid = hand[2]
    rank = top_score - ind
    score = (bid*rank)
    print(f'{hand} score={score} rank={rank} bid={bid}')
    scores +=  score
print(scores)
