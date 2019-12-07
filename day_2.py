import copy


def opcode1(opcode_position, ints):
    ints[ints[opcode_position + 3]] = (
        ints[ints[opcode_position + 1]] + ints[ints[opcode_position + 2]])


def opcode2(opcode_position, ints):
    ints[ints[opcode_position + 3]] = (
        ints[ints[opcode_position + 1]] * ints[ints[opcode_position + 2]])


def process(ints):
    i = 0
    while i <= len(ints):
        if ints[i] == 1:
            opcode1(i, ints)
            i += 4
        elif ints[i] == 2:
            opcode2(i, ints)
            i += 4
        elif ints[i] == 99:
            break
        else:
            print("something went wrong!")
            break


def test_puzzle1():
    tests = [
        [
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]],
        [[1, 0, 0, 0, 99], [2, 0, 0, 0, 99]],
        [[2, 3, 0, 3, 99], [2, 3, 0, 6, 99]],
        [[2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]],
        [[1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]],
    ]

    for test in tests:
        process(test[0])
        assert test[0] == test[1], "{} != {}".format(test[0], test[1])


if __name__ == "__main__":
    test_puzzle1()
    inp = []
    with open("day_2.txt", "r") as f:
        data = f.readline()
        inp = [int(i) for i in data.split(",")]

    inp_copy = copy.deepcopy(inp)
    inp_copy[1] = 12
    inp_copy[2] = 2
    process(inp_copy)
    print("puzzle1", inp_copy[0])

    is_break = False
    for noun in range(100):
        for verb in range(100):
            data = copy.deepcopy(inp)
            data[1] = noun
            data[2] = verb
            process(data)
            if data[0] == 19690720:
                print("puzzle2 {}".format(noun * 100 + verb))
                is_break = True
                break
        if is_break:
            break
