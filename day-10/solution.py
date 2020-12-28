"""
--- Day 10: Adapter Array ---
TODO: FINISH PUZZLE 2
"""
_ADAPTERS = []

def calculate(index, tally=None):
    """
    Sub function for puzzle 2
    """
    if tally is None:
        tally = [0] * len(_ADAPTERS)
        tally[-1] = 1

    if _ADAPTERS[index] == 0:
        return tally[1]

    current_joltage = _ADAPTERS[index]
    perm_total = 0

    if (top_index := index + 4) > 0:
        top_index = 0
        for i in range(index + 1, top_index):
            jolt = _ADAPTERS[i]
            if jolt - current_joltage <= 3:
                print("VALID: %s - %s"%(jolt, current_joltage))
                print(tally[i])
                perm_total += tally[i]
                tally[i] = perm_total
                print("Total: %s"%(perm_total))

                tally[index] = perm_total

    return calculate(index - 1, tally)


def puzzle2():
    """
    I did look at r/AdventOfCode for a little help, but mainly just learned the pattern
    of factorials wrt permutations. For example, if we have a list of adapters like this:
    [0] 1 2 3 4 [7]
     ^
    We would have 7 different ways to go from 0 -> 7 (all valid permutations end in 4)
    0 1 2 3 4
    0 1 2 4
    0 1 3 4
    0 1 4
    --
    0 2 3 4
    0 2 4
    --
    0 3 4
    """
    result = calculate(-2)
    return result


def puzzle1():
    """
    Solves puzzle 1
    """
    one_jolt_diff = 0
    three_jolt_diff = 0

    for i in range(1, len(_ADAPTERS)):
        difference = _ADAPTERS[i] - _ADAPTERS[i - 1]
        if difference == 1:
            one_jolt_diff += 1
        elif difference == 3:
            three_jolt_diff += 1
    return one_jolt_diff * three_jolt_diff


if __name__ == "__main__":
    with open("input.txt") as file:
        _LINE_LIST = file.read().splitlines()
        _ADAPTERS = [int(adapter) for adapter in _LINE_LIST]
        _ADAPTERS.append(0)
        _ADAPTERS.sort()
        _ADAPTERS.append(_ADAPTERS[-1] + 3)

        _PRODUCT = puzzle1()
        print(_PRODUCT)

        _TOTAL = puzzle2()
        print(_TOTAL)
