# Implementation of binary search algorithm
# differentiating binary and regular search
import random
import time

def regular_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# assuming we're iterating through a sorted array
def binary_search(l, target, high=None, low=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l(midpoint) == target:
        return midpoint
    elif target < l(midpoint):
        return binary_search(l, target, midpoint, target - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)


if __name__ == "__main__":
    # l = [1, 3, 7, 10, 12, 19, 20]
    # target = 10
    # print(regular_search(l, 10))
    # print(binary_search(l, 10))
    length = 1000
    sorted_list = set()
    while len(sorted_list) < length:
            sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        regular_search(sorted_list, target)
    end = time.time()
    print("Regular search took: ", (end - start)/length, "seconds")
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search took:", (end - start)/length, "seconds")

