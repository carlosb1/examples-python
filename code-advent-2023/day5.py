import sys
from pathlib import Path

DEFAULT_FILE = 'day5.txt'


def parse_entry(lines, start, end):
    mapped = []
    for line in lines[start+1:end]:
        parsed_line = line.strip().split(' ')
        destination = int(parsed_line[0])
        source = int(parsed_line[1])
        range_ = int(parsed_line[2])
        mapped.append([source, source + range_, destination])
    return mapped

def run():
    if len(sys.argv) < 2:
        filepath = Path(DEFAULT_FILE)
    else:
        filepath = Path(sys.argv[1])

    f = filepath.open()
    lines = f.readlines()
    seeds = lines[0].split(":")[1].strip().split()
    seed_to_soil_index = lines.index('seed-to-soil map:\n')
    seed_to_soil_index_end = lines.index("\n",seed_to_soil_index)
    soil_to_fertilizer_index = lines.index('soil-to-fertilizer map:\n')
    soil_to_fertilizer_index_end = lines.index("\n",soil_to_fertilizer_index)

    fertilizer_to_water_index = lines.index('fertilizer-to-water map:\n')
    fertilizer_to_water_index_end = lines.index('\n',fertilizer_to_water_index)
    water_to_light_index = lines.index('water-to-light map:\n')
    water_to_light_index_end = lines.index('\n',water_to_light_index)
    light_to_temperature_index = lines.index('light-to-temperature map:\n')
    light_to_temperature_index_end = lines.index('\n',light_to_temperature_index)
    temperature_to_humidity_index = lines.index('temperature-to-humidity map:\n')
    temperature_to_humidity_index_end = lines.index('\n',temperature_to_humidity_index)
    humidity_to_location_index = lines.index('humidity-to-location map:\n')
    humidity_to_location_index_end = len(lines)


    seed_to_soil = parse_entry(lines, seed_to_soil_index, seed_to_soil_index_end)
    soil_to_fertilizer  = parse_entry(lines, soil_to_fertilizer_index, soil_to_fertilizer_index_end)
    fertilizer_to_water = parse_entry(lines, fertilizer_to_water_index, fertilizer_to_water_index_end)
    water_to_light  = parse_entry(lines, water_to_light_index, water_to_light_index_end)
    light_to_temperature = parse_entry(lines, light_to_temperature_index, light_to_temperature_index_end)
    temperature_to_humidity  = parse_entry(lines, temperature_to_humidity_index, temperature_to_humidity_index_end)
    humidity_to_location = parse_entry(lines, humidity_to_location_index, humidity_to_location_index_end)


    def get_mapped(list_mapped, entry):
        result = entry
        for mapped in list_mapped:
            if entry >= mapped[0] and entry <= mapped[1] :
                result = mapped[2] + (entry - mapped[0])
                break
        return result


    locations = []
    for seed in seeds:
        seed = int(seed)

        soil =  get_mapped(seed_to_soil, seed)
        fertilizer =  get_mapped(soil_to_fertilizer, soil)
        water = get_mapped(fertilizer_to_water, fertilizer)
        light = get_mapped(water_to_light, water)
        temperature = get_mapped(light_to_temperature, light)
        humidity = get_mapped(temperature_to_humidity, temperature)
        location = get_mapped(humidity_to_location, humidity)
        locations.append(location)

    print(locations)
    print(min(locations))
if __name__ == '__main__':
    run()


