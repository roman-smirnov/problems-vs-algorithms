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
    # This is a binary search problem
    high = number + 1
    low = 0

    while low < high-1:
        mid = int((high + low) / 2)
        if mid**2 > number:
            high = mid
        else:
            low = mid
        print(low, mid, high)
    return low


if __name__ == '__main__':
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
