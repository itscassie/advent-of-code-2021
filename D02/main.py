""" Solve 2021 Day 2: Dive! Problem """

def parse_input(txt_path):
    """parse input TXT file to list of list"""
    with open(txt_path, encoding="UTF-8") as file:
        str_input = [line.split() for line in file]
        input_list = [[line[0], int(line[1])] for line in str_input]
    return input_list


def solver_problem1(input_list):
    """walk through the route and return horizon * depth"""
    horizon = 0
    depth = 0
    for direction, distance in input_list:
        if direction == "forward":
            horizon += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance

    return horizon * depth


def solver_problem2(input_list):
    """walk through the route and return aim"""
    horizon = 0
    depth = 0
    aim = 0
    for direction, distance in input_list:
        if direction == "forward":
            horizon += distance
            depth = depth + aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance

    return horizon * depth


if __name__ == "__main__":
    data = parse_input("./input/d02.txt")
    print(solver_problem1(data))
    print(solver_problem2(data))
