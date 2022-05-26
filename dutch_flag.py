""" Dutch National Flag """


def swap(fnum, snum, array):
    temp = array[fnum]
    array[fnum] = array[snum]
    array[snum] = temp


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    if input_list is None:
        raise ValueError('input_list should not be None')
    if not input_list:
        raise ValueError('input_list should not be empty')

    input_list = input_list.copy()
    low = 0
    mid = 0
    high = len(input_list) - 1
    while mid <= high:
        if input_list[mid] == 0:
            swap(low, mid, input_list)
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        elif input_list[mid] == 2:
            swap(mid, high, input_list)
            high -= 1
        else:
            raise ValueError
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    # print(test_case)
    # print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


def none_test():
    try:
        sort_012(None)
    except Exception as e:
        print(e)  # should print 'input_list should not be None'


def empty_test():
    try:
        sort_012([])
    except Exception as e:
        print(e)  # should print 'input_list should not be Empty'


def my_test():
    inlist = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    outlist = sort_012(inlist)
    # print(inlist)
    # print(outlist)


def single_test():
    print(sort_012([0]))  # should print '[0]'


def duo_test():
    print(sort_012([1, 0]))  # should print '[0.1]'
    print(sort_012([2, 0]))  # should print '[0.2]'
    print(sort_012([2, 1]))  # should print '[1.2]'


def large_test():
    array = [i % 3 for i in range(100000)]
    print('Pass') if sort_012(array) == sorted(array) else print('Fail')    # should print 'Pass'


if __name__ == '__main__':
    none_test()
    empty_test()
    single_test()
    duo_test()
    large_test()
    my_test()
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
