""" Max and Min in a Unsorted Array """

import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if ints is None:
        raise ValueError('ints should not be None')
    if not ints:
        raise ValueError('ints should not be empty')
    if len(ints) < 2:
        raise ValueError('ints should have at least 2 elements')

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


def none_test():
    try:
        get_min_max(None)
    except Exception as e:
        print(e)  # should print 'ints should not be None'


def empty_test():
    try:
        get_min_max([])
    except Exception as e:
        print(e)  # should print 'ints should not be Empty'


def single_test():
    try:
        get_min_max([1])
    except Exception as e:
        print(e)  # should print 'ints should have at least 2 elements'


def large_test():
    array = [i % 99 for i in range(100000)]
    print('Pass') if get_min_max(array) == (min(array), max(array)) else print('Fail')  # should print 'Pass'


if __name__ == '__main__':
    none_test()
    empty_test()
    single_test()
    large_test()
    my_test()
