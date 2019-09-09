'''
https://leetcode.com/problems/expression-add-operators/
282. Expression Add Operators
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
'''


class Solution(object):
  def helper(self, num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    for i in range(len(num)):
      result = []
      if num[i] == '#':
        left_result_list = self.helper(num[:i], target)
        right_result_list = self.helper(num[i+1:], target)



  def addOperators(self, num, target):
    num = str(num)
    temp = ''
    for i in num: temp += i + '#'
    num = temp[:len(temp) - 1]
    return self.helper(num, target)


if __name__ == '__main__':
  sol = Solution()
  num, target = 123, 6
  print(sol.addOperators(num, target))