# Merge Sort algo
'''Divide: Divide the list or array recursively into two halves until it can no more be divided.
Conquer: Each subarray is sorted individually using the merge sort algorithm.
Merge: The sorted subarrays are merged back together in sorted order.
The process continues until all elements from both subarrays have been merged.'''

def mergeSort(lst):
    # Base case
    if len(lst) <= 1:
        return lst

    # Find mid index and split list into 2 sublists
    mid = len(lst) // 2
    left_sublist = mergeSort(lst[:mid])
    right_sublist = mergeSort(lst[mid:])

    # This list includes sorted elements
    buffer = []
    # End the loop only when one of the two sublists has no more elements
    while len(left_sublist) != 0 and len(right_sublist) != 0:
        if left_sublist[0] < right_sublist[0]:
            buffer.append(left_sublist[0])
            left_sublist.pop(0)
        else:
            buffer.append(right_sublist[0])
            right_sublist.pop(0)

    # Add the remaining elements of the remaining sublist to the buffer
    if len(left_sublist) == 0:
        buffer.extend(right_sublist)
    else:
        buffer.extend(left_sublist)

    return buffer

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = mergeSort(unsorted_list)
print(sorted_list)

