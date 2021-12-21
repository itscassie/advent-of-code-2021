""" Solve 2021 Day 7: The Treachery of Whales Problem """

def parse_input(txt_path):
    """parse input TXT file to initial crab position"""
    with open(txt_path, encoding="UTF-8") as file:
        f = file.readline()
        position = f.strip().split(",")
        position = [int(i) for i in position]

    return position


def solver_problem1(position):
    """input position and return min fuel cost of alignment"""
    min_fuel = float("Inf")
    for i in range(min(position), max(position)):
        dist = [0] * len(position)
        dist = [abs(position[j] - i) for j in range(len(position))]
        min_fuel = min(min_fuel, sum(dist))

    return min_fuel


def solver_problem2(position):
    """input position and return min fuel cost of alignment with linear costs"""
    min_fuel = float("Inf")
    for i in range(min(position), max(position)):
        dist = [0] * len(position)
        dist = [
            abs(position[j] - i) * (abs(position[j] - i) + 1) // 2
            for j in range(len(position))
        ]
        min_fuel = min(min_fuel, sum(dist))

    return min_fuel


if __name__ == "__main__":
    crab_pos = parse_input("./input/d07.txt")
    # print(crab_pos)

    output1 = solver_problem1(crab_pos)
    print(output1)

    output2 = solver_problem2(crab_pos)
    print(output2)
