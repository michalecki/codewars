'''
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals,
and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals are represented by a pair of integers in the form of an array. The first value of
the interval will always be less than the second value. Interval example: [1, 5] is an interval
from 1 to 5. The length of this interval is 4.

List containing overlapping intervals:
[
   [1,4],
   [7, 10],
   [3, 5]
]

The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat
the interval as [1, 5], which has a length of 4.
'''


def sum_intervals(inp_arr):
    '''

    :param array: array of intervals
    :return: sum of lengths of the intervals
    '''

    # sort the intervals over the first digit
    inp_arr.sort()
    # loop and merge if overlap
    i = 0
    while i < len(inp_arr) - 1:
        while inp_arr[i][1] >= inp_arr[i + 1][0]:
            inp_arr[i] = [inp_arr[i][0], max(inp_arr[i + 1][1], inp_arr[i][1])]
            del inp_arr[i + 1]
            if i == len(inp_arr) - 1:
                break
        i += 1
    # calculate the sum
    total = sum([inp_arr[x][1] - inp_arr[x][0] for x in range(len(inp_arr))])

    return total


# testing
sum_intervals([
    [1, 2],
    [6, 10],
    [11, 15]
])  # \; // => 9

sum_intervals([
    [1, 4],
    [7, 10],
    [3, 5]
])  # ; // => 7

sum_intervals([
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11]
])  # ; // => 19
