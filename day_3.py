class Point():
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "x = {}, y = {}".format(self.X, self.Y)

    def __eq__(self, other_point):
        return self.X == other_point.X and self.Y == other_point.Y


class Line():
    def __init__(self, start_point, end_point):
        if start_point.X == end_point.X:
            self.is_horizontal = False
            self.X = start_point.X
            self.Y_min = min(start_point.Y, end_point.Y)
            self.Y_max = max(start_point.Y, end_point.Y)
        else:
            self.is_horizontal = True
            self.Y = start_point.Y
            self.X_min = min(start_point.X, end_point.X)
            self.X_max = max(start_point.X, end_point.X)

        self.start_point = start_point


def get_total_step(move):
    return int(move[1:])


def get_wire(path):
    x, y = 0, 0
    wire = []
    steps = 0

    moves = path.split(",")
    for move in moves:
        start_point = Point(x, y)
        direction = move[0]
        total_step = get_total_step(move)
        if direction == "R":
            x += total_step
        elif direction == "L":
            x -= total_step
        elif direction == "U":
            y += total_step
        elif direction == "D":
            y -= total_step
        else:
            print("something wrong")

        end_point = Point(x, y)
        wire.append([Line(start_point, end_point), steps])
        steps += total_step
    return wire


def is_cross(line1, line2):
    if line1.start_point == Point(0, 0) and line2.start_point == Point(0, 0):
        return False
    if line1.is_horizontal == line2.is_horizontal:
        return False

    if line1.is_horizontal:
        return (
            line2.Y_min <= line1.Y <= line2.Y_max) and (
                line1.X_min <= line2.X <= line1.X_max
            )

    return (
        line1.Y_min <= line2.Y <= line1.Y_max) and (
            line2.X_min <= line1.X <= line2.X_max
        )


def get_cross_point(line1, line2):
    if line1.is_horizontal:
        return Point(line2.X, line1.Y)
    return Point(line1.X, line2.Y)


def get_closest_cross_point_distance(wire1, wire2):
    closest_cross_point_distance = 0
    for line1, _ in wire1:
        for line2, _ in wire2:
            if is_cross(line1, line2):
                cross_point = get_cross_point(line1, line2)
                cross_point_distance = get_distance(cross_point)
                if (closest_cross_point_distance == 0) or (
                    closest_cross_point_distance > cross_point_distance
                ):
                    closest_cross_point_distance = cross_point_distance
    return closest_cross_point_distance


def get_minimize_signal_delay(wire1, wire2):
    minimize_signal_delay = 0
    for line1, steps1 in wire1:
        for line2, steps2 in wire2:
            if is_cross(line1, line2):
                cross_point = get_cross_point(line1, line2)
                cross_point_steps = steps1 + steps2 + (
                    get_steps_to_cross_point(line1, cross_point)) + (
                        get_steps_to_cross_point(line2, cross_point))
                if (minimize_signal_delay == 0) or (
                    minimize_signal_delay > cross_point_steps
                ):
                    minimize_signal_delay = cross_point_steps
    return minimize_signal_delay


def get_distance(point):
    return abs(point.X) + abs(point.Y)


def get_steps_to_cross_point(line, cross_point):
    return abs(line.start_point.X - cross_point.X) + abs(
        line.start_point.Y - cross_point.Y)


class TestClass():
    def __init__(self, line1, line2, is_cross, cross_point):
        self.line1 = line1
        self.line2 = line2
        self.is_cross = is_cross
        self.cross_point = cross_point


def test_get_cross_point():
    tests = [
        TestClass(
            Line(Point(0, 0), Point(10, 0)),
            Line(Point(2, 3), Point(2, -3)),
            True,
            Point(2, 0)),
        TestClass(
            Line(Point(0, 0), Point(10, 0)),
            Line(Point(2, 3), Point(2, 5)),
            False,
            None,),
        TestClass(
            Line(Point(0, 0), Point(10, 0)),
            Line(Point(3, 0), Point(6, 0)),
            False,
            None),
        ]

    for test in tests:
        assert is_cross(test.line1, test.line2) == test.is_cross
        if test.is_cross:
            assert test.cross_point == get_cross_point(test.line1, test.line2)


def test_get_closest_cross_point_distance():
    tests = [
        ("R8,U5,L5,D3", "U7,R6,D4,L4", 6),
        (
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83",
            159),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            135,
        ),
    ]

    for test in tests:
        wire1 = get_wire(test[0])
        wire2 = get_wire(test[1])
        closest_cross_point = get_closest_cross_point_distance(wire1, wire2)
        assert closest_cross_point == test[2]


def test_get_minimize_signal_delay():
    tests = [
        ("R8,U5,L5,D3", "U7,R6,D4,L4", 30),
        (
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83",
            610),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            410,
        ),
    ]

    for test in tests:
        wire1 = get_wire(test[0])
        wire2 = get_wire(test[1])
        minimize_signal_delay = get_minimize_signal_delay(wire1, wire2)
        assert minimize_signal_delay == test[2], "{} != {}".format(
            minimize_signal_delay, test[2])


if __name__ == "__main__":
    test_get_cross_point()
    test_get_closest_cross_point_distance()
    test_get_minimize_signal_delay()

    with open("day_3.txt", "r") as f:
        line1 = f.readline()
        line2 = f.readline()
        wire1 = get_wire(line1)
        wire2 = get_wire(line2)
        print("puzzle1", get_closest_cross_point_distance(wire1, wire2))
        print("puzzle2", get_minimize_signal_delay(wire1, wire2))
