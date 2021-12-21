""" Solve 2021 Day8: Seven Segment Search Problem """
import numpy as np


def parse_input(txt_path):
    """parse input TXT file to wire list and four digits list"""
    with open(txt_path, encoding="UTF-8") as file:
        wires_list = []
        digits_list = []
        for line in file:
            wires, digits = line.strip().split(" | ")
            wires_list.append(wires.split(" "))
            digits_list.append(digits.split(" "))

    return wires_list, digits_list


def solver_problem1(digits_list):
    """input digits and return numbers that 1, 4, 7, 8 occurs"""
    cnt = 0
    for digits in digits_list:
        for d in digits:
            if len(d) in [2, 3, 4, 7]:
                cnt += 1
    return cnt


def solver_problem2(wires_list, digits_list):
    """input wires pattern, digits list and returns summmation of all 4 digit number"""
    number_sum = 0
    for wires, digits in zip(np.array(wires_list), np.array(digits_list)):
        wire_lens = np.array([len(w) for w in wires])
        digit_wires = ["" for _ in range(10)]
        digit_wires[1] = wires[wire_lens == 2].item()
        digit_wires[4] = wires[wire_lens == 4].item()
        digit_wires[7] = wires[wire_lens == 3].item()
        digit_wires[8] = wires[wire_lens == 7].item()
        wire_069 = wires[wire_lens == 6]
        wire_235 = wires[wire_lens == 5]

        # 9
        set_147 = (
            set(digit_wires[1]).union(set(digit_wires[4])).union(set(digit_wires[7]))
        )
        idx_9 = [set_147.issubset(set(wire.item())) for wire in wire_069].index(1)
        digit_wires[9] = wire_069[idx_9].item()

        # 0/6
        wire_06 = np.delete(wire_069, idx_9)
        if set(digit_wires[1]).issubset(set(wire_06[0].item())):
            digit_wires[0] = wire_06[0].item()
            digit_wires[6] = wire_06[1].item()
        else:
            digit_wires[0] = wire_06[1].item()
            digit_wires[6] = wire_06[0].item()

        # 2/3/5
        idx_3 = [set(digit_wires[1]).issubset(set(wire.item())) for wire in wire_235]
        digit_wires[3] = wire_235[idx_3].item()
        wire_25 = np.delete(wire_235, idx_3)
        idx_5 = [set(wire.item()).issubset(digit_wires[6]) for wire in wire_25]
        digit_wires[5] = wire_25[idx_5].item()
        digit_wires[2] = np.delete(wire_25, idx_5).item()

        digit_wires = ["".join(sorted(dw)) for dw in digit_wires]

        num = ""
        for dig in digits:
            dig = "".join(sorted(dig))
            num += str(digit_wires.index(dig))
        number_sum += int(num)

    return number_sum


if __name__ == "__main__":
    wires_l, digits_l = parse_input("./input/d08.txt")

    count = solver_problem1(digits_l)
    print(count)

    total = solver_problem2(wires_l, digits_l)
    print(total)
