""" Solve 2021 Day 6: Lanternfish Problem """
from collections import defaultdict
import numpy as np


def parse_input(txt_path):
    """parse input TXT file to initial state list"""
    with open(txt_path, encoding="UTF-8") as file:
        f = file.readline()
        init_state = f.strip().split(",")
        init_state = [int(i) for i in init_state]

    return init_state


def solver_problem1(init_state, day):
    """input initial state and day and output fish number on this day"""
    day_n = np.array(init_state[:], dtype=np.int16)

    for _ in range(day):
        zero_num = (day_n == 0).sum()
        zero_idx = day_n == 0
        non_zero_idx = day_n != 0

        day_n[zero_idx] += 6
        day_n[non_zero_idx] -= 1
        day_n = np.append(day_n, 8 * np.ones((1, zero_num), dtype=np.int16))

    return len(day_n)


def update_fish(fish_library):
    """update fish library every day"""
    new_fish_lib = defaultdict(int)
    for timer, n_fish in fish_library.items():
        if timer == 0:
            timer = 7
            new_fish_lib[8] += n_fish
        new_fish_lib[timer - 1] += n_fish
    return new_fish_lib


def solver_problem2(init_state, day):
    """
    input initial state, day and output fish
    a more efficiet way that only record a fish library with {timer: fish number}
    """
    fish_lib = {timer: init_state.count(timer) for timer in set(init_state)}
    for _ in range(day):
        fish_lib = update_fish(fish_lib)

    return sum(fish_lib.values())


if __name__ == "__main__":

    init_fish = parse_input("./input/d06.txt")
    output1 = solver_problem1(init_fish, 80)
    print(output1)

    output2 = solver_problem2(init_fish, 256)
    print(output2)
