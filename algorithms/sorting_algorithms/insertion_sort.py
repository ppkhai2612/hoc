# Insertion Sort algo
def insertionSort(lst):
    # The number of iterations for a given list, start with the second element
    for i in range(1, len(lst)):
        j = i
        # Compare the current element with its already sorted left part
        while lst[j-1] > lst[j] and j > 0:
            buffer = lst[j]
            lst[j] = lst[j-1]
            lst[j-1] = buffer
            j -= 1
    return lst


unsorted_list = [19, 2, 31, 45, 30, 11, 121, 27]
sorted_list = insertionSort(unsorted_list)
print(sorted_list)