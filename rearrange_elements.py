""" Rearrange Array Elements """
from queue import PriorityQueue


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        raise ValueError('input_list should not be None')
    if not input_list:
        raise ValueError('input_list should not be empty')
    if len(input_list) < 2:
        raise ValueError('input_list should have at least 2 elements')

    min_heap = PriorityQueue()
    for item in input_list:
        min_heap.put(item)

    num1 = 0
    num2 = 0
    j = 0
    for i in range(len(input_list)):
        if i % 2 == 0:
            num1 += min_heap.get() * 10 ** j
        else:
            num2 += min_heap.get() * 10 ** j
            j += 1

    print('num1:', num1, 'num2:', num2)
    return [num1, num2]


def none_test():
    try:
        rearrange_digits(None)
    except Exception as e:
        print(e)  # should print 'input_list should not be None'


def empty_test():
    try:
        rearrange_digits([])
    except Exception as e:
        print(e)  # should print 'input_list should not be Empty'


def single_test():
    try:
        rearrange_digits([1])
    except Exception as e:
        print(e)  # should print 'input_list should have at least 2 elements'


def large_test():
    print(rearrange_digits([i % 10 for i in range(11)]))  # should print '[975310, 86420]'


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    none_test()
    empty_test()
    single_test()
    large_test()
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
