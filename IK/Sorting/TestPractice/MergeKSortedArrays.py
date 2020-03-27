"""
Merge_K_sorted_arrays

Problem Statement:

This is a popular facebook problem.
Given K sorted arrays arr, of size N each, merge them into a new array res, such that res is a sorted array.

Assume N is very large compared to K. N may not even be known. The arrays could be just sorted streams, for instance, timestamp streams.

All arrays might be sorted in increasing manner or decreasing manner. Sort all of them in the manner they appear in input.

Note:
Repeats are allowed.
Negative numbers and zeros are allowed.
Assume all arrays are sorted in the same order. Preserve that sort order in output.
It is possible to find out the sort order from at least one of the arrays.

Input/Output Format For The Function:

Input Format:

There is only one argument: 2D Integer array arr.
Here, arr[i][j] denotes value at index j of ith input array, 0-based indexing. So, arr is K * N size array.

Output Format:

Return an integer array res, containing all elements from all individual input arrays combined.

Input/Output Format For The Custom Input:

Input Format:

The first line of input should contain an integer K. The second line should contain an integer N, denoting size of each input array.
In next K lines, ith line should contain N space separated integers, denoting content of ith array of K input arrays, where jth element in this ith line is nothing but arr[i][j], i.e. value at index j of ith array, 0-based indexing.

If K = 3, N = 4 and arr = [
[1, 3, 5, 7],
            [2, 4, 6, 8],
            [0, 9, 10, 11]
], then input should be:

3
4
1 3 5 7
2 4 6 8
0 9 10 11

Output Format:

There will be (N*K) lines of output, where ith line contains an integer res[i], denoting value at index i of res.
Here, res is the result array returned by solution function.

For input K = 3, N = 4 and arr = [
[1, 3, 5, 7],
            [2, 4, 6, 8],
            [0, 9, 10, 11]
], output will be:

0
1
2
3
4
5
6
7
8
9
10
11

Constraints:
1 <= N <= 500
1 <= K <= 500
-10^6 <= arr[i][j] <= 10^6, for all valid i,j

Sample Test Case:

Sample Input:

K = 3, N =  4
arr[][] = { {1, 3, 5, 7},
           {2, 4, 6, 8},
           {0, 9, 10, 11}} ;

Sample Output:

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
"""
import heapq

def mergeArrays(arr):
  if not arr: return arr
  if len(arr) == 1: return arr[0]
  # ascertain sort order
  ascending = False if arr[0][len(arr[0]) - 1] < arr[0][0] else True
  # handle descending order
  min_heap = []
  for i in range(len(arr)):
    value = arr[i][0] if ascending else (-1 * arr[i][0])
    min_heap.append((value, i, 0))
  heapq.heapify(min_heap)

  result = []
  while min_heap:
    temp, i, j = heapq.heappop(min_heap)
    value = temp if ascending else (-1 * temp)
    result.append(value)
    if j + 1 < len(arr[i]):
      value = arr[i][j + 1] if ascending else (-1 * arr[i][j + 1])
      heapq.heappush(min_heap, (value, i, j + 1))
  return result


if __name__ == '__main__':
  arr = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
  arr = [
    [34, 26, 20, 13, 11, 7, 4, 4],
    [41, 34, 27, 23, 19, 10, 8, 0],
    [26, 25, 19, 12, 7, 7, 7, 5],
    [46, 39, 35, 33, 27, 19, 12, 9],
    [33, 24, 22, 18, 18, 10, 3, 0],
    [42, 35, 35, 30, 21, 20, 12, 9],
    [42, 33, 24, 21, 12, 12, 8, 7],
    [29, 23, 21, 18, 18, 11, 8, 7],
    [35, 30, 30, 23, 15, 14, 8, 7],
    [20, 18, 17, 16, 12, 11, 5, 4]
  ]
  print(mergeArrays(arr))
