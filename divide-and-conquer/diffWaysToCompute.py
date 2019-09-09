'''
https://leetcode.com/problems/different-ways-to-add-parentheses/
241. Different Ways to Add Parentheses
https://youtu.be/gxYV8eZY0eQ
'''
class Solution(object):
  def diffWaysToCompute(self, input):
    """
    :type input: str
    :rtype: List[int]
    """
    # validate input
    def isoperator(char):
      return char == '+' or char == '-' or char == '*'

    def operate(left, right, operator):
      if operator == '+':
        return left + right
      elif operator == '-':
        return left - right
      else:
        return left * right

    def diffWaysToComputeHelper(input):
      result = []
      for i in range(len(input)):
        if isoperator(input[i]):
          # found an operator divide
          k = input[i]
          left_result = diffWaysToComputeHelper(input[:i])
          right_result = diffWaysToComputeHelper(input[i+1:])
          # conquer
          for left_result_element in left_result:
            for right_result_element in right_result:
              result.append(operate(left_result_element, right_result_element, input[i]) )
      if len(result) == 0:
        # found no operator, convert the string to int and append to the result
        result.append(int(input))
      return result

    return diffWaysToComputeHelper(input)

if __name__ == '__main__':
    sol = Solution()
    # input = "13"
    # input = "2*3-4*5"
    input = "2-1-1"
    print(sol.diffWaysToCompute(input))