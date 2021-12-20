""" Solve 2021 Day 5: Hydrothermal Venture Problem """
import numpy as np


def parse_input(txt_path, diag=False):
    """parse input TXT file to filtered coordinates list"""
    with open(txt_path, encoding="UTF-8") as file:
        coordinate_list = []
        for line in file:
            count = False
            cor1, cor2 = line.strip().split(" -> ")
            x1, y1 = (int(cor1.split(",")[0]), int(cor1.split(",")[1]))
            x2, y2 = (int(cor2.split(",")[0]), int(cor2.split(",")[1]))
            # filter with horizontal/vertical lines
            if x1 == x2 or y1 == y2:
                count = True
            elif diag:
                # filter 45 degree lines
                if (x2 - x1) == (y2 - y1) or (x2 - x1) == (y1 - y2):
                    count = True

            if count:
                coordinate_list.append([(x1, y1), (x2, y2)])

    return coordinate_list


def solver_problem1(coordinate_list):
    """input list turn it into count diagram and output values > 2 or larger"""
    diagram = np.zeros(
        (np.max(coordinate_list[:][:]) + 1, np.max(coordinate_list[:][:]) + 1),
        dtype=np.int16,
    )
    for _, ((x1, y1), (x2, y2)) in enumerate(coordinate_list):
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        if x1 == x2:
            diagram[y_min : y_max + 1, x_min] += 1
        elif y1 == y2:
            diagram[y_min, x_min : x_max + 1] += 1

    points_num = (diagram >= 2).sum()
    return points_num


def solver_problem2(coordinate_list):
    """
    input list turn it into count diagram and output values > 12 or larger
    take 45 degree in to count
    """
    diagram = np.zeros(
        (np.max(coordinate_list[:][:]) + 1, np.max(coordinate_list[:][:]) + 1),
        dtype=np.int16,
    )
    for _, ((x1, y1), (x2, y2)) in enumerate(coordinate_list):
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                diagram[y_min : y_max + 1, x_min] += 1
            elif y1 == y2:
                diagram[y_min, x_min : x_max + 1] += 1
        elif (x2 - x1) == (y2 - y1):
            for i in range(0, x_max - x_min + 1):
                # (x1, y1) => (x1 + 1, y1 + 1) = > (x2, y2)
                diagram[y_min + i, x_min + i] += 1
        elif (x2 - x1) == (y1 - y2):
            for i in range(0, x_max - x_min + 1):
                # (x_max, y_min) = > (x_max - 1, y_min + 1) => (x_min, y_max)
                diagram[y_min + i, x_max - i] += 1
    points_num = (diagram >= 2).sum()
    return points_num


if __name__ == "__main__":
    coor_list = parse_input("./input/d05.txt")
    # print(coor_list)
    output1 = solver_problem1(coor_list)
    print(output1)

    coor_list = parse_input("./input/d05.txt", diag=True)
    output2 = solver_problem2(coor_list)
    print(output2)
