# Shell Sort algo
'''Make the array h-sorted for a large value of h.
We keep reducing the value of h until it becomes 1.
An array is said to be h-sorted if all sublists of every h’th element are sorted.'''

def shellSort(lst):
    gap = len(lst) // 2
    while gap > 0: # End the loop when gap == 0
        for idx in range(gap, len(lst)): # Traverse from gap'th element to end of the list
            cur_val = lst[idx]

            # Compare current element with the element whose distance is gap
            while lst[idx - gap] > cur_val and idx >= gap:
                lst[idx] = lst[idx - gap]
                idx -= gap
            lst[idx] = cur_val
        gap //= 2 # Reducing gap by 2

    return lst


unsorted_list = [19, 2, 31, 45, 30, 11, 121, 27]
sorted_list = shellSort(unsorted_list)
print(sorted_list)