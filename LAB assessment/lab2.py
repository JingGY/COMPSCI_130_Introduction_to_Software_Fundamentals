import math


def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    while (min_index <= max_index):
        mid_index = math.floor((max_index+min_index)/2)
        if numbers[mid_index] == value:
            return mid_index
        elif numbers[mid_index] < value:
            min_index = mid_index + 1
        elif numbers[mid_index] > value:
            max_index = mid_index - 1
    return -1


numbers = [10, 15, 20, 27, 41, 69]
print(binary_search(numbers, 69))

numbers = [13, 18, 54, 61, 78, 93]
print(binary_search(numbers, 7))
