import math


def get_fuel(mass):
    return math.floor(mass / 3) - 2


def get_total_fuel(mass, total):
    if mass <= 6:
        return total
    else:
        mass = get_fuel(mass)
        total += mass
        return get_total_fuel(mass, total)


def test_get_fuel():
    assert get_fuel(12) == 2
    assert get_fuel(14) == 2
    assert get_fuel(1969) == 654
    assert get_fuel(100756) == 33583


def test_get_total_fuel():
    tests = [
        (1969, 966),
        (100756, 50346),
    ]

    for test in tests:
        total = get_total_fuel(test[0], 0)
        assert total == test[1], "{} != {}".format(total, test[1])


if __name__ == "__main__":
    test_get_fuel()
    test_get_total_fuel()
    total_puzzle2 = 0
    total_puzzle1 = 0
    with open("day_1.txt", "r") as f:
        data = f.readlines()

        for line in data:
            total_puzzle1 += get_fuel(int(line))
            total_puzzle2 += get_total_fuel(int(line), 0)

    print("puzzle1", total_puzzle1)
    print("puzzle2", total_puzzle2)
