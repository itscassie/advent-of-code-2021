""" Solve 2021 Day9: Smoke Basin Problem """

def parse_input(txt_path):
    """parse input TXT file to input list"""
    inputs = []
    with open(txt_path, encoding="UTF-8") as file:
        for line in file:
            inputs.append([int(x) for x in line.strip()])
    return inputs


def get_point(inputs, x, y):
    """return point[x][y] if in the boundary, return None if not"""
    if x < 0 or y < 0 or x >= len(inputs) or y >= len(inputs[0]):
        return None
    return inputs[x][y]


def is_lowest(inputs, x, y):
    """return if lowest flag"""
    neighbors = []
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if get_point(inputs, x + i, y + j) is not None:
            neighbors.append(get_point(inputs, x + i, y + j))
    return inputs[x][y] < min(neighbors)


def solver_problem1(inputs):
    """input list and return risk level based on lowest points"""
    risk_level = 0
    low_points = []
    for i in range(len(inputs)):
        for j in range(len(inputs[0])):
            if is_lowest(inputs, i, j):
                risk_level += 1 + inputs[i][j]
                low_points.append([i, j])
    return risk_level, low_points


def get_neighbor(inputs, x, y):
    """return neighbor points if it's valid"""
    neighbors = []
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if get_point(inputs, x + i, y + j) is not None:
            neighbors.append([x + i, y + j])
    return neighbors


def expand_enighbor(low_point, inputs):
    """given the lowest point and return its neighbor"""
    result = set()

    while len(low_point) != 0:
        [x, y] = low_point.pop()
        result.add((x, y))
        for (i, j) in get_neighbor(inputs, x, y):
            if inputs[i][j] != 9 and (i, j) not in result and (i, j) not in low_point:
                low_point.append([i, j])
    return result


def solver_problem2(inputs, low_points):
    """
    Flood Fill problem.
    We keep track of which nodes (positions in the 2d array)
    we've already visited, and run a DFS for each
    """
    flood_sizes = []

    for p in low_points:
        flood_sizes.append(len(expand_enighbor([p], inputs)))
    flood_sizes.sort()

    return flood_sizes[-1] * flood_sizes[-2] * flood_sizes[-3]


if __name__ == "__main__":
    inp_points = parse_input("./input/d09.txt")

    r_level, l_points = solver_problem1(inp_points)
    print(r_level)

    flood_mul = solver_problem2(inp_points, l_points)
    print(flood_mul)
