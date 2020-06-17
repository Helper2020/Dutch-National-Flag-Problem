"""
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal.
For e.g. if you traverse the array twice, that would still be an O(n) solution
but it will not count as single traversal.
"""


def sort_012(arr):
    l_idx = 0
    r_idx = len(arr) - 1
    front_idx = 0

    while front_idx <= r_idx:
        if arr[front_idx] == 0:
            swap(arr, l_idx, front_idx)
            l_idx += 1
            front_idx += 1
        elif arr[front_idx] == 1:
            front_idx += 1
        else:
            swap(arr, r_idx, front_idx)
            r_idx -= 1

    return arr


def swap(arr, idx, front_idx):
    temp = arr[idx]
    arr[idx] = arr[front_idx]
    arr[front_idx] = temp


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Edge cases
# All zeroes
test_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# Empty list
test_function([])
#------------------
test_function([2, 1, 0, 2, 1])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1])
