import copy


def opcode1(opcode_position, param1_position, param2_position, ints):
    ints[ints[opcode_position + 3]] = (
        ints[param1_position] + ints[param2_position])


def opcode2(opcode_position, param1_position, param2_position, ints):
    ints[ints[opcode_position + 3]] = (
        ints[param1_position] * ints[param2_position])


def opcode3(opcode_position, inp, ints):
    ints[ints[opcode_position + 1]] = inp


def opcode4(opcode_position, ints):
    return ints[ints[opcode_position + 1]]


def param_modes(params, opcode_position, ints):
    params_str = str(params)
    params_str = "0" * (5 - len(params_str)) + params_str

    param2_mode = int(params_str[1])
    param1_mode = int(params_str[2])
    opcode = int(params_str[3:])

    return opcode, param1_mode, param2_mode


def get_params_position(opcode_position, param1_mode, param2_mode, ints):
    param1_position, param2_position = opcode_position + 1, opcode_position + 2
    if param1_mode == 0:
        param1_position = ints[param1_position]
    if param2_mode == 0:
        param2_position = ints[param2_position]

    return param1_position, param2_position


def process(ints, inp):
    i = 0
    while i <= len(ints):
        opcode, param1_mode, param2_mode = param_modes(
            ints[i], i, ints)
        param1_position, param2_position = get_params_position(
            i, param1_mode, param2_mode, ints)
        if opcode == 1:
            opcode1(i, param1_position, param2_position, ints)
            i += 4
        elif opcode == 2:
            opcode2(i, param1_position, param2_position, ints)
            i += 4
        elif opcode == 3:
            opcode3(i, inp, ints)
            i += 2
        elif opcode == 4:
            out = opcode4(i, ints)
            i += 2
        elif ints[i] == 99:
            break
        else:
            print("something wrong", i, ints[i])

    return out


if __name__ == "__main__":
    inp = []
    with open("day_5.txt", "r") as f:
        data = f.readline()
        inp = [int(i) for i in data.split(",")]

    inp_copy = copy.deepcopy(inp)
    print("puzzle1", process(inp_copy, 1))
