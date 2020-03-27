# class Solution:
#   def generate_expression(nums, operators):
#     expression = str(nums[0])
#     for i in range(1, len(nums)):
#       operator = operators[i-1]
#       if operator == '|':
#         operator = ''
#       elif operator == '*':
#         operator = '*'
#       else:
#         operator = '+'
#       expression += operator + str(nums[i])
#     return expression
#
#   def operate(left, right, operator):
#     if operator == '|':
#       return int(str(left) + str(right))
#     elif operator == '*':
#       return left * right
#     else:
#       return left + right
#
#   def evaluate(nums, operators, target):
#     temp_nums = nums[:]
#     print(operators)
#     for operator in operators:
#       left_operant = temp_nums.pop()
#       right_operant = temp_nums.pop()
#       temp_result = operate(left_operant, right_operant, operator)
#       temp_nums.append(temp_result)
#     if temp_nums[0] == target:
#       ret = generate_expression(nums, operators)
#       return ret
#     return None
#
#   def helper(nums, operators, slate, result, length, target):
#     if len(slate) == length:
#       ret = evaluate(nums, slate, target)
#       if ret: result.append(ret)
#       return
#
#     for operator in operators:
#       slate.append(operator)
#       helper(nums, operators, slate, result, length, target)
#       slate.pop()
#
#   def generate_all_expressions(nums, target):
#     numbers, operators, slate, result, length = [int(i) for i in nums], ['|', '*', '+'], [], [], len(nums)-1
#     helper(numbers, operators, slate, result, length, target)
#     return result

from collections import deque


# def foo(a, b, op):
#   if op == '+':
#     return int(a) + int(b)
#   else:
#     return int(a) * int(b)


# def myeval(expression):
#   operands = deque()
#   operators = deque()
#   current_number = ''
#   for item in expression:
#     if item.isnumeric():
#       current_number += item
#     else:
#       operators.append(item)
#       temp = int(current_number)
#       operands.append(str(temp))
#       current_number = ''
#   operands.append(int(current_number))
#
#   for operator in operators:
#     a = operands.popleft()
#     b = operands.popleft()
#     operands.append(foo(a, b, operator))
#   return operands.popleft()

# def myeval(expression, memo):
#   if expression.isnumeric():
#     return str(int(expression))
#
#   if expression in memo:
#     return memo[expression]
#
#   expr = ''
#   current_number = ''
#   for item in expression:
#     if item.isnumeric():
#       current_number += item
#     else:
#       expr += str(int(current_number))
#       current_number = ''
#       expr += item
#   expr += str(int(current_number))
#   memo[expression] = str(eval(expr))
#   return memo[expression]
#
#
# def helper(params, nums_index, slate, slate_val, result, memo):
#
#   # if myeval(slate) > params['target']:
#   #   return
#
#   # if slate in params['memo']:
#   #   slate = params['memo'][slate]
#   # else:
#   #   params['memo'][slate] = myeval(slate)
#
#   # if nums_index == len(params['nums']):
#   #   if int(slate_val) == params['target']:
#   #     result.append(slate)
#   #   return
#   if nums_index == len(params['nums']):
#     if int(myeval(slate, memo)) == params['target']:
#       result.append(slate)
#     return
#
#   for op in params['operators']:
#     # print(slate_val, op, params['nums'][nums_index])
#     # expr =
#     helper(
#       params,
#       nums_index + 1,
#       slate + op + params['nums'][nums_index],
#       myeval(slate_val + op + params['nums'][nums_index], memo),
#       result,
#       memo
#     )
#   pass
#
# def generate_all_expressions(nums, target):
#   operators = ['', '+', '*']
#   nums_index = 1
#   slate = nums[0]
#   slate_val = nums[0]
#   result = []
#   memo = {}
#   params = {
#     'nums': nums,
#     'operators': operators,
#     'target': target,
#   }
#   helper(
#     params,
#     nums_index,
#     slate,
#     slate_val,
#     result,
#     memo
#   )
#   return result

# def generate_all_expressions(nums, target):
#   def operate(a, b, operator):
#     if operator == '':
#       return a + b
#     elif operator == '+':
#       return str(int(a) + int(b))
#     elif operator == '-':
#       return str(int(a) - int(b))
#     elif operator == '*':
#       return str(int(a) * int(b))
#     else:
#       return str(int(a) // int(b))
#
#   def operation(slate, last_operand, last_operator, current_operand, current_operator):
#     precedence = {
#       '': 3,
#       '*': 2,
#       '/': 2,
#       '+': 1,
#       '-': 1,
#     }
#
#     undo = {
#       '+': '-',
#       '-': '+',
#       '*': '/',
#       '/': '*',
#     }
#
#     temp_slate = None
#     if precedence[current_operator] > precedence[last_operator]:
#       undone_slate = operate(slate, last_operand, undo[last_operator])
#       current_temp = operate(last_operand, current_operand, current_operator)
#       temp_slate = operate(undone_slate, current_temp, last_operator)
#     else:
#       temp_slate = operate(slate, current_operand, current_operator)
#     return temp_slate
#
#   def helper(nums_index, last_operand, last_operator, slate, expr):
#     # base
#     if nums_index == len(nums):
#       if int(slate) == target:
#         result.append(expr[:])
#       return
#
#     for op in operators:
#       # ''
#       temp_slate = operation(slate, last_operand, last_operator, nums[nums_index], op)
#       helper(nums_index+1, nums[nums_index], '', temp_slate, expr[:] + op + nums[nums_index])
#       pass
#
#
#   nums_index = 0
#   last_operand = '0'
#   last_operator = ''
#   slate = '0'
#   result = []
#   operators = ['', '+', '*']
#   expr = ''
#   helper(nums_index, last_operand, last_operator, slate, expr)
#   return result

# def generate_all_expressions(s, target):
#   n = len(s)
#
#   def helper(i, prev, total, sofar, op):
#     if i == n:
#       if total == target:
#         op.append(sofar)
#       return
#     for j in range(i, n):
#       curr = s[i:j + 1]
#       curr_val = int(curr)
#       print(curr_val)
#       if i == 0:
#         helper(j + 1, curr_val, curr_val, curr, op)
#       else:
#         helper(j + 1, curr_val, total + curr_val, sofar + "+" + curr, op)
#         helper(j + 1, prev * curr_val, total - prev + (prev * curr_val), sofar + "*" + curr, op)
#     return
#
#   res = []
#   helper(0, 0, 0, "", res)
#   return res

def operate(a, b, operator):
  if operator == '':
    return a + b
  elif operator == '+':
    return str(int(a) + int(b))
  elif operator == '-':
    return str(int(a) - int(b))
  elif operator == '*':
    return str(int(a) * int(b))
  else:
    return str(int(a) // int(b))

def myeval(s):
  precedence = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
  }
  pre_eval = 0
  curr_eval = 0
  pre_op = '+'
  curr_op = '+'
  index  = 0
  len_s = len(s)
  while index < len_s:
    if s[index].isdigit():
      curr_number = ''
      while index < len_s and s[index].isdigit():
        curr_number += s[index]
        index += 1
      curr_number = int(curr_number)
      if precedence[curr_op] >= precedence[pre_op]:
        curr_eval = operate(curr_eval, curr_number, curr_op)
      else:
        curr_eval = operate(curr_eval, curr_number, curr_op)
        curr_eval = operate(pre_eval, curr_eval, pre_op)
    else:
      if precedence[s[index]] > precedence[curr_op]:
        curr_op = s[index]
      else:
        pre_op = curr_op
        curr_op = s[index]
      index += 1
  return curr_eval


if __name__ == '__main__':
  # # nums, target = '222', 24
  # # nums, target = '050505', 5
  # nums, target = '1234', 11
  # # nums, target = '40404040', 0
  # # nums, target = '00000000001', 1
  # # nums, target = '0000000000000', 0
  # result = generate_all_expressions(nums, target)
  # print(len(result), result)
  s = '2+3*4*2+1'
  print(myeval(s))