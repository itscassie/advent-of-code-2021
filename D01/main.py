""" Solve 2021 Day 1: Sonar Sweep Problem """
def solver_problem1(inputs):
    """ Count the number of increasement from given list """
    num_increased = 0
    for i in range(1, len(inputs)):
        if inputs[i] > inputs[i - 1]:
            num_increased += 1
    return num_increased


def solver_problem2(inputs):
    """ Count the number of increasement from each sum of 3 number from give list """
    num_increased = 0
    for i in range(1, len(inputs) - 2):
        # sum_prev = inputs[i-1] + inputs[i] + inputs[i+1]
        # sum_curr = inputs[i] + inputs[i+1] + inputs[i+2]
        # (sum_curr - sum_prev) = inputs[i+2] - inputs[i-1]
        if inputs[i + 2] > inputs[i - 1]:
            num_increased += 1
    return num_increased


if __name__ == "__main__":
    with open("./input/d01.txt", encoding='UTF-8') as file:
        data = [int(line.strip()) for line in file]
    print(solver_problem1(data))
    print(solver_problem2(data))
