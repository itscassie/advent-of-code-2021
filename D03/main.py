""" Solve 2021 Day 3: Binary Diagnostic Problem """


def parse_input(txt_path):
    """parse input TXT file to list of binary numbers"""
    with open(txt_path, encoding="UTF-8") as file:
        str_list = [list(line.strip()) for line in file]
        input_list = [list(map(int, str_item)) for str_item in str_list]
    return input_list


# Checklist:
# ensure all binaries are same length
# ensure there are odd number of lines
def solver_problem1(input_list):
    """walk through the binaries and calculate the most/least common bit"""
    common_bit = [0] * len(input_list[0])
    for _, bin_list in enumerate(input_list):
        for j, bin_num in enumerate(bin_list):
            if bin_num == 1:
                common_bit[j] += 1
            else:
                common_bit[j] -= 1

    gamma_rate = []
    epsilon_rate = []
    for _, bit_num in enumerate(common_bit):
        if bit_num > 0:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            gamma_rate.append(0)
            epsilon_rate.append(1)

    gamma_strs = [str(integer) for integer in gamma_rate]
    gamma_ints = int("".join(gamma_strs), 2)

    epsilon_strs = [str(integer) for integer in epsilon_rate]
    epsilon_ints = int("".join(epsilon_strs), 2)

    return gamma_ints * epsilon_ints


def count_most(lines, bit_idx):
    """input desire lines, bit index and output the most common bit"""
    count_bit = 0
    for line in lines:
        if line[bit_idx] == 1:
            count_bit += 1
        else:
            count_bit -= 1
    most_bit = 1 if count_bit >= 0 else 0

    return most_bit


def solver_problem2(input_list):
    """input code list and return oxygen/co2 rating"""
    # for i in range(len(input_list[0])):
    # (1) walk through curr list, get most bit
    # (2) walk through curr list, keep list idx with most/least bit
    # (3) update curr list
    oxygen_list = input_list.copy()
    while len(oxygen_list) > 1:
        for i in range(len(input_list[0])):
            most_bit = count_most(oxygen_list, i)
            keep_idx = []
            for j, bin_list in enumerate(oxygen_list):
                if bin_list[i] == most_bit:
                    keep_idx.append(j)
            oxygen_list = [oxygen_list[idx] for idx in keep_idx]

            if len(oxygen_list) < 2:
                oxygen_strs = [str(integer) for integer in oxygen_list[0]]
                oxygen_rating = int("".join(oxygen_strs), 2)
                break

    co2_list = input_list.copy()
    while len(co2_list) > 1:
        for i in range(len(input_list[0])):
            most_bit = count_most(co2_list, i)
            keep_idx = []
            for j, bin_list in enumerate(co2_list):
                if bin_list[i] != most_bit:
                    keep_idx.append(j)
            co2_list = [co2_list[idx] for idx in keep_idx]

            if len(co2_list) < 2:
                co2_strs = [str(integer) for integer in co2_list[0]]
                co2_rating = int("".join(co2_strs), 2)
                break

    return oxygen_rating * co2_rating


if __name__ == "__main__":
    data = parse_input("./input/d03.txt")
    print(solver_problem1(data))
    print(solver_problem2(data))
