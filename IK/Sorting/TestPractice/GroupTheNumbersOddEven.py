"""
https://leetcode.com/problems/sort-array-by-parity/submissions/

Given an array A of non-negative integers, return an array consisting of all the even elements of A,
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
************************************************************************************************
From IK web
************************************************************************************************
Group the numbers

Problem Statement:

You are given an integer array arr, of size n. Group and rearrange them (in-place) into evens and odds in such
a way that group of all even integers appears on the left side and group of all odd integers appears on the right side.

Input/Output Format For The Function:

Input Format:

There is only one argument: Integer array arr.

Output Format:

Return the same integer array, with evens on left side and odds on the right side.
There is no need to preserve order within odds or within evens.

Input/Output Format For The Custom Input:

Input Format:

The first line of input should contain an integer n, denoting size of input array arr. In next n lines, ith line should contain an integer arr[i], denoting a value at index i of arr.

If n = 4 and arr = [1, 2, 3, 4], then input should be:

4
1
2
3
4

Output Format:

There will be n lines of output, where ith line contains an integer res[i], denoting value at index i of res.
Here, res is the result array returned by solution function.

For input n = 4 and arr = [1, 2, 3, 4], output will be:

4
2
1
3

Constraints:
1 <= n <= 10^5
arr contains only positive integers.
arr may contains duplicate numbers.
Solution with linear time complexity and constant auxiliary space is expected.

Sample Test Case:

Sample Input:

[1, 2, 3, 4]

Sample Output:

[4, 2, 1, 3]

Explanation:

Order does not matter. Other valid solution are
[2, 4, 1, 3]
[2, 4, 3, 1]
[4, 2, 3, 1]
"""

from typing import *

class Solution:
  def sortArrayByParity(self, A: List[int]) -> List[int]:
    def is_odd(num):
      return num % 2

    if not A: return -1
    if len(A) == 1: return A
    even = -1
    for index, value in enumerate(A):
      if not is_odd(value):
        even += 1
        A[even], A[index] = A[index], A[even]
    return A


if __name__ == '__main__':
  arr = [1, 2, 3, 4]
  sol = Solution()
  print(sol.sortArrayByParity(arr))



