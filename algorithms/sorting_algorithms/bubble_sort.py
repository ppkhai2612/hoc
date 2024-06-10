# Bubble sort algo
'''Traverse from left and compare adjacent elements and the higher one is placed at right side.
In this way, the largest element is moved to the rightmost end at first.
This process is then continued to find the second largest and place it and so on until the data is sorted.'''

def bubbleSort(lst):
    for iter_num in range(len(lst)-1, 0, -1):
        for idx in range(iter_num):
            if lst[idx] > lst[idx+1]:
                buffer = lst[idx]
                lst[idx] = lst[idx+1]
                lst[idx+1] = buffer
    return lst


unsorted_list = [19, 2, 31, 45, 6, 11, 21, 27]
sorted_list = bubbleSort(unsorted_list)
print(sorted_list)