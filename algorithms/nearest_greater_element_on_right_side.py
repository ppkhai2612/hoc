# NGE's of array elements
from bisect import bisect_right as upper_bound, \
    bisect_left as lower_bound


# Function to print the NGE
def printNGE(a: list, n):
    ms = set()

    # insert in the multiset container
    for i in range(n):
        ms.add(a[i])

    print("Element NGE", end="")

    # Required because Python sets
    # are not sorted
    new_arr = list(ms)
    new_arr.sort()

    # traverse for all array elements
    for i in range(n):

        # find the upper_bound in set
        it = upper_bound(new_arr, a[i])

        # if points to the end, then
        # no NGE of that element
        if (it == len(new_arr)):
            print("\n %d ----> -1" % a[i], end="")

        # print the element at that position
        else:
            print("\n %d ----> %d" % (a[i],
                                      new_arr[it]), end="")

        # find the first occurrence of
        # the index element and delete it
        it = lower_bound(new_arr, a[i])

        # delete one occurrence
        # from the container
        new_arr.remove(new_arr[it])


# Driver Code
a = [4, 5, 2, 25]
n = len(a)
# Function call to print the NGE
printNGE(a, n)

