""" Search in a Rotated Sorted Array """


# [4, 5, 6, 7, 0, 1, 2]
# [5,6,7,0,1,2,4]
# [2,4,5,6,7,0,1]
# [0,1,2,4,5,6,7]
def find_max(array):
    """ use binary search to find the argmax of the sorted rotated array """
    low = 0
    high = len(array) - 1
    while low < high - 1:
        pivot = int((low + high) / 2)
        # print('low: ', low, 'mid: ', pivot, 'high: ', high)
        if array[pivot] > array[high]:
            low = pivot
        elif array[pivot] < array[low]:
            high = pivot
        else:
            return high
    return low


def binary_search(array, value):
    """ use binary search to find the index of a value in a sorted array """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        # print('low: ', low, 'mid: ', mid, 'high: ', high)
        if array[mid] > value:
            high = mid - 1
        elif array[mid] < value:
            low = mid + 1
        else:
            return mid
    return -1


# [[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # 1. find the max in O(logn)
    # 2. divide the array from begining to the argmax and from the argmax to the end of the array
    # 3. use binary search on each subarray to find the sought after value
    argmax = find_max(input_list)
    argmin = 0 if argmax == len(input_list) - 1 else argmax + 1
    # print('argmin: ', argmin, 'argmax: ', argmax)
    if argmin < argmax:
        return binary_search(input_list, number)
    result = binary_search(input_list[argmin:], number)
    if result != -1:
        return result + argmin
    result = binary_search(input_list[:argmax+1], number)
    if result != -1:
        return result
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def test_find_max():
    assert find_max([4, 5, 6, 7, 0, 1, 2]) == 3, 'test 1 failed in test_find_max() '
    assert find_max([5, 6, 7, 0, 1, 2, 4]) == 2, 'test 2 failed in test_find_max() '
    assert find_max([2, 4, 5, 6, 7, 0, 1]) == 4, 'test 3 failed in test_find_max() '
    assert find_max([0, 1, 2, 4, 5, 6, 7]) == 6, 'test 4 failed in test_find_max() '
    print('all tests in test_find_max() passed!')


def test_binary_search():
    assert binary_search([0, 1, 2, 4, 5, 6, 7], 7) == 6, 'test 1 failed in test_binary_search() '
    assert binary_search([0, 1, 2, 4, 5, 6, 7], 0) == 0, 'test 1 failed in test_binary_search() '
    assert binary_search([0, 1, 2, 4, 5, 6, 7], 3) == -1, 'test 1 failed in test_binary_search() '
    print('all tests in test_binary_search() passed!')


if __name__ == '__main__':
    test_find_max()
    test_binary_search()
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
