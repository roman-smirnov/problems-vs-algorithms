""" Max and Min in a Unsorted Array """

import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    argmax = 0
    argmin = 0
    for i in range(len(ints)):
        if ints[i] > ints[argmax]:
            argmax = i
        if ints[i] < ints[argmin]:
            argmin = i

    return ints[argmin], ints[argmax]


def my_test():
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print(l)
    print(get_min_max(l))
    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


if __name__ == '__main__':
    my_test()
