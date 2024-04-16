'''Find the Maximun Number in an Array
Write a Java program to find the largest number in an array of integers.
Expect:
Input: [5, 10, 3, 20, 8]
Output: The largest number in the array is 20

Input: [12, 15, 8, 27, 6]
Output: The largest number in the array is 27'''

def find_max(numbers):
    max_number = numbers[0]
    for i in numbers:
        if i > max_number:
            max_number = i
    return max_number


maximum_number = find_max([5, 10, 3, 20, 8])
print(f'The largest number in the array is {maximum_number}')