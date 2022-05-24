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


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
