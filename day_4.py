def is_double_list(i1, i2, i3, i4, i5, i6):
    return i1 == i2 or i2 == i3 or i3 == i4 or i4 == i5 or i5 == i6


def is_not_decrease_list(i1, i2, i3, i4, i5, i6):
    return i1 <= i2 and i2 <= i3 and i3 <= i4 and i4 <= i5 and i5 <= i6


def is_double_list_puzzle2(i1, i2, i3, i4, i5, i6):
    group_by = {}
    for i in (i1, i2, i3, i4, i5, i6):
        if i in group_by:
            group_by[i] += 1
        else:
            group_by[i] = 1
    for v in group_by.values():
        if v == 2:
            return True
    return False


def test_is_double_list_puzzle2():
    tests = [
        ("112233", True),
        ("123444", False),
        ("111122", True),
        ]
    for v, b in tests:
        assert is_double_list_puzzle2(v[0], v[1], v[2], v[3], v[4], v[5]) == b


if __name__ == "__main__":
    total = 0
    for i in range(158126, 624574):
        str_i = str(i)
        i1, i2, i3, i4, i5, i6 = (
            str_i[0], str_i[1], str_i[2],
            str_i[3], str_i[4], str_i[5])
        if is_double_list(i1, i2, i3, i4, i5, i6) and (
            is_not_decrease_list(i1, i2, i3, i4, i5, i6)
        ):
            total += 1
    print("puzzle1", total)

    total = 0
    for i in range(158126, 624574):
        str_i = str(i)
        i1, i2, i3, i4, i5, i6 = (
            str_i[0], str_i[1], str_i[2],
            str_i[3], str_i[4], str_i[5])
        if is_double_list(i1, i2, i3, i4, i5, i6) and (
            is_not_decrease_list(i1, i2, i3, i4, i5, i6)
        ) and (is_double_list_puzzle2(i1, i2, i3, i4, i5, i6)):
            total += 1
    print("puzzle2", total)
