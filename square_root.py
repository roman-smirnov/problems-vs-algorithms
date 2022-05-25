""" Square Root of an Integer
Find the square root of the integer without using any Python library
"""


def sqrt(number: int):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        raise ValueError('number must not be None')
    if not isinstance(number, int):
        raise ValueError('number must be an int')

    # This is a binary search problem
    high = number + 1
    low = 0

    while low < high - 1:
        mid = int((high + low) / 2)
        if mid ** 2 > number:
            high = mid
        else:
            low = mid
    return low


def none_test():
    try:
        sqrt(None)
    except Exception as e:
        print(e)  # shoud print 'number must not be None'


def int_test():
    try:
        sqrt(float('inf'))
    except Exception as e:
        print(e)  # shoud print 'number must be an int'


def zero_test():
    print("Pass" if (0 == sqrt(0)) else "Fail")  # shoud print 'Pass'


def one_test():
    print("Pass" if (1 == sqrt(1)) else "Fail")  # shoud print 'Pass'


def provided_tests():
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")


if __name__ == '__main__':
    none_test()
    int_test()
    one_test()
    provided_tests()
