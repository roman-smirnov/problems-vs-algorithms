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


def my_test():
    inlist = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    outlist = sort_012(inlist)
    print(inlist)
    print(outlist)


if __name__ == '__main__':
    # my_test()
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
