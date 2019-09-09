'''
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
718. Maximum Length of Repeated Subarray
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].


Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''
class Solution(object):
  def findLength(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    # memo = [[None] * (len(B) + 1) for _ in range(len(A) + 1)]
    curr = [None] * (len(B) + 1)
    prev = [None] * (len(B) + 1)
    result = 0
    for i in range(len(A) + 1):
      for j in range(len(B) + 1):
        if i == 0 or j == 0 or A[i - 1] != B[j - 1]:
          curr[j] = 0
        else:
          curr[j] = prev[j - 1] + 1
          result = max(result, curr[j])
      prev, curr = curr, prev
    return result

if __name__ == '__main__':
  sol = Solution()
