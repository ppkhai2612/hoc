# Quick Sort algorithm
'''Picks an element as a pivot
and partitions the given array around the picked pivot
by placing the pivot in its correct position in the sorted array.'''

import statistics, random

def quickSort(numbers):
    if len(numbers) <= 1:
        return numbers

    else:
        # Find pivot element
        pivot = statistics.median([numbers[0], numbers[len(numbers) // 2], numbers[-1]])
        lesser_items, pivot_items, greater_items = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot]
        )

        return quickSort(lesser_items) + pivot_items + quickSort(greater_items)


def getRandomNumbers(length, minimum=1, maximum=100):
    numbers = []
    for _ in range(length):
        numbers.append(random.randint(minimum, maximum))
    return numbers


numbers = getRandomNumbers(8, 100, 1000)
sorted_numbers = quickSort(numbers)
print(sorted_numbers)
