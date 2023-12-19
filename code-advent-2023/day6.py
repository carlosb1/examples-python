import sys
from pathlib import Path

DEFAULT_FILE = 'day6.txt'

if len(sys.argv) < 2:
    filepath = Path(DEFAULT_FILE)
else:
    filepath = Path(sys.argv[1])

lines = [' '.join(line.split()) for line in  filepath.open().readlines()]
time = lines[0].strip().split(' ')[1:]
distance = lines[1].strip().split(' ')[1:]

num_races = len(time)

def mills_per_millm(millisec,boost):
    return millisec * boost

def append(distances, distance, record):
    if distance > record:
        distances.append(distance)

all_distances = []
num_race = 0
while num_race < num_races:
    lasts_mills = int(time[num_race])
    race_distance = int(distance[num_race])
    print(f'lasts_mills={lasts_mills} race_distance={race_distance}')

    # possible movements
    distances = []
    for boost_mill in range(0, lasts_mills+1):
        if boost_mill == 0:
            continue
        if boost_mill > lasts_mills:
            continue
        mills_in_movement = lasts_mills - boost_mill
        dist = mills_per_millm(mills_in_movement, boost_mill)
        append(distances, dist, race_distance)
    num_race+=1
    all_distances.append(distances)

print(all_distances)
accm = 1
results = [len(distance) for distance in all_distances]
for temp_resul in results:
    accm*= temp_resul
print(accm)



