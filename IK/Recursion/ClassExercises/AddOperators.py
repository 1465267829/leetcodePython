"""
https://leetcode.com/problems/expression-add-operators/

282. Expression Add Operators

Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

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
"""

from typing import *

# class Solution:
#     def addOperators(self, num: str, target: int) -> List[str]:
#       def myeval(slate):
#         return eval(slate)
#
#       def helper(index, slate):
#         if index == N:
#           eval_slate = myeval(slate)
#           if eval_slate == target: result.append(slate[:])
#           return
#
#         for op in ops:
#           if op == '' and num[index - 1] == '0': continue
#           helper(
#             index+1,
#             slate + op + num[index]
#           )
#         pass
#
#       if not num: return []
#       ops = ['+', '-', '*', '']
#       slate = num[0]
#       result = []
#       N = len(num)
#       index = 1
#       helper(index, slate)
#       return result

class Solution:
  def addOperators(self, num: str, target: int) -> List[str]:
    def backtracking(i: int = 0, prefix: str = '', value: int = 0, prev: int = 0):
      if i == len(num) and value == target:
        result.append(prefix)
        return None
      for j in range(i + 1, len(num) + 1):
        string = num[i:j]
        number = int(string)
        if string != '0' and num[i] == '0': continue
        if not prefix:
          backtracking(j, string, number, number)
        else:
          backtracking(j, prefix + '+' + string, value + number, number)
          backtracking(j, prefix + '-' + string, value - number, -number)
          backtracking(j, prefix + '*' + string, value - prev + prev * number, prev * number)

    result = []
    backtracking()
    return result







if __name__ == '__main__':
  sol = Solution()
  ip = [
    ['123', 6], # ["1+2+3", "1*2*3"]
    # ['123', 5], # ["1+2+3", "1*2*3"]
    # ['232', 8], # ["2*3+2", "2+3*2"]
    # ['00', 0],  # ["0+0", "0-0", "0*0"]
    # ['105', 5],# ["1*0+5","10-5"]
    # ['123456789', 45],
    # # ['050505', 5],
    # ['1232537859', 995],
  ]
  for nums, target in ip:
    ret = sol.addOperators(nums, target)
    for x in ret:
      assert eval(x) == target, x
    print(len(ret), ret)

