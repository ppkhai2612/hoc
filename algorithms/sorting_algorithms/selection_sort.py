# Selection Sort algo
'''Selects the smallest (or largest) element from the unsorted portion of the list
and swaps it with the first element of the unsorted part.
This process is repeated for the remaining unsorted portion until the entire list is sorted.'''

def selectionSort(lst):
    # This loop iterates through the list
    for outer_idx in range(len(lst) - 1):
        min_idx = outer_idx
        # This loop find the min idx
        for inner_idx in range(outer_idx + 1, len(lst)):
            if lst[inner_idx] < lst[min_idx]:
                min_idx = inner_idx
        lst[outer_idx], lst[min_idx] = lst[min_idx], lst[outer_idx] # Swap the min value with the compared value

    return lst

unsorted_list = [19, 2, 31, 45, 30, 11, 121, 27]
sorted_list = selectionSort(unsorted_list)
print(sorted_list)