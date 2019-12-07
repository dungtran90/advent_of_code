def update_orbit_map(orbit_data, orbit_map):
    orbit = orbit_data.split(")")[1]
    obj = orbit_data.split(")")[0]

    if orbit in orbit_map:
        orbit_map[orbit].append(obj)
    else:
        orbit_map[orbit] = [obj]


def update_reverse_orbit_map(orbit_data, reverse_orbit_map):
    orbit = orbit_data.split(")")[1]
    obj = orbit_data.split(")")[0]

    if obj in reverse_orbit_map:
        reverse_orbit_map[obj].append(orbit)
    else:
        reverse_orbit_map[obj] = [orbit]


def count_orbits(orbit_map):
    total = 0
    for k, v in orbit_map.items():
        total += count_orbits_with_key(k, orbit_map)
    return total


def count_orbits_with_key(key, orbit_map):
    total = 0
    keys = orbit_map[key]
    while(len(keys) > 0):
        keys_temp = []
        for k in keys:
            total += 1
            if k in orbit_map:
                keys_temp.extend(orbit_map[k])
        keys = keys_temp

    return total


def test_count_orbits():
    test_data = "COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L"
    orbit_map = {}
    for orbit_data in test_data.split(","):
        update_orbit_map(orbit_data, orbit_map)
    assert count_orbits(orbit_map) == 42


def from_you_to_san(orbit_map, reverse_orbit_map):
    keys = ["YOU"]
    distance = 0

    while(len(keys) > 0):
        keys_temp = []
        for key in keys:
            if key in orbit_map:
                keys_temp.extend(orbit_map[key])
            if key in reverse_orbit_map:
                keys_temp.extend(reverse_orbit_map[key])
        if "SAN" in keys_temp:
            break
        distance += 1
        keys = list(set(keys_temp))

    return distance - 1


def test_from_you_to_san():
    test_data = "COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L,K)YOU,I)SAN"
    orbit_map = {}
    reverse_orbit_map = {}
    for orbit_data in test_data.split(","):
        update_orbit_map(orbit_data, orbit_map)
        update_reverse_orbit_map(orbit_data, reverse_orbit_map)
    assert from_you_to_san(orbit_map, reverse_orbit_map) == 4


if __name__ == "__main__":
    test_count_orbits()
    test_from_you_to_san()

    orbit_map = {}
    reverse_orbit_map = {}
    with open("day_6.txt", "r") as f:
        for line in f:
            update_orbit_map(line.strip(), orbit_map)
            update_reverse_orbit_map(line.strip(), reverse_orbit_map)

    print("puzzle1", count_orbits(orbit_map))
    print("puzzle2", from_you_to_san(orbit_map, reverse_orbit_map))
