""" Solve 2021 Day 4: Giant Squid Problem """
import numpy as np


def parse_input(txt_path):
    """parse input TXT file to number list and list of bingo tables"""
    with open(txt_path, encoding="UTF-8") as file:
        num_str = file.readline().strip().split(",")
        num_list = [int(num) for num in num_str]

        table_list = []
        for i, line in enumerate(file):
            if i % 6 == 0:
                table = []
            else:
                num_str = line.strip().replace("  ", " ").split(" ")
                num_row = [int(num) for num in num_str]
                table.append(num_row)
                if i % 6 == 5:
                    table_list.append(table)

    return num_list, np.array(table_list)


def solver_problem1(num_list, table_list):
    """input num_list, tables and determine which table bingo first"""
    bingo_flag = False
    # initialize bingo count table
    row_cnt = [0] * table_list.shape[1]
    col_cnt = [0] * table_list.shape[2]
    bingo_cnt = []
    for i in range(table_list.shape[0]):
        bingo_cnt.append([row_cnt, col_cnt])
    bingo_cnt = np.array(bingo_cnt)

    # enmerate num_list
    for i, num in enumerate(num_list):
        for j, table in enumerate(table_list):
            r, c = np.where(table == num)
            r = r.item() if len(r) == 1 else -1
            c = c.item() if len(c) == 1 else -1
            if r != -1:
                bingo_cnt[j, 0, r] += 1
                bingo_cnt[j, 1, c] += 1
        bingo_flag = True if len(np.where(bingo_cnt == 5)[0]) != 0 else False

        if bingo_flag:
            bingo_idx = np.where(bingo_cnt == 5)[0]
            bingo_table = table_list[bingo_idx]
            marked_sum = 0
            for k in range(0, i + 1):
                if len(np.where(bingo_table == num_list[k])[0]) != 0:
                    marked_sum += num_list[k]
            unmarked_sum = np.sum(table_list[bingo_idx]) - marked_sum
            return num * unmarked_sum


def solver_problem2(num_list, table_list):
    """input num_list, tables and determine which table bingo last"""
    bingo_flag = False
    is_last = False
    all_table = set([i for i in range(table_list.shape[0])])

    # initialize bingo count table
    row_cnt = [0] * table_list.shape[1]
    col_cnt = [0] * table_list.shape[2]
    bingo_cnt = []
    for i in range(table_list.shape[0]):
        bingo_cnt.append([row_cnt, col_cnt])
    bingo_cnt = np.array(bingo_cnt)

    # enmerate num_list
    for i, num in enumerate(num_list):
        for j, table in enumerate(table_list):
            r, c = np.where(table == num)
            r = r.item() if len(r) == 1 else -1
            c = c.item() if len(c) == 1 else -1
            if r != -1:
                bingo_cnt[j, 0, r] += 1
                bingo_cnt[j, 1, c] += 1
        bingo_flag = True if len(np.where(bingo_cnt >= 5)[0]) != 0 else False

        # keep bingo indexs to find last table
        if bingo_flag:
            bingo_idxs = set(np.where(bingo_cnt >= 5)[0])
            if len(bingo_idxs) == table_list.shape[0] - 1:
                last_idx = [key for key in (all_table - bingo_idxs)]
            elif len(bingo_idxs) == table_list.shape[0]:
                is_last = True

        # when last table wins
        if is_last:
            marked_sum = 0
            bingo_table = table_list[last_idx[0]]
            for k in range(0, i + 1):
                if len(np.where(bingo_table == num_list[k])[0]) != 0:
                    marked_sum += num_list[k]
            unmarked_sum = np.sum(bingo_table) - marked_sum
            return num * unmarked_sum


if __name__ == "__main__":
    numbers, tables = parse_input("./input/d04.txt")
    print(solver_problem1(numbers, tables))
    print(solver_problem2(numbers, tables))
