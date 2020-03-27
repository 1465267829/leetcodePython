def helper(num_left, num_right, slate, result):
  # backtracking case
  if num_left < 0 or num_right < 0 or num_left > num_right:
    # if we ran out of left or right parenthesis then we clearly
    # won't have any legal combination anymore
    # OR
    # or if number of left parenthesis are more than
    # number of right parenthesis, then we clearly won't have any legal
    # permutation anymore
    return

  # base case:
  if num_left == 0 and num_right == 0:
    result.append(''.join(slate))
    return

  # recursive case
  slate.append('(')
  helper(num_left - 1, num_right, slate, result)
  slate.pop()

  slate.append(')')
  helper(num_left, num_right - 1, slate, result)
  slate.pop()
  return


def find_all_well_formed_brackets(n):
  num_left, num_right, slate, result = n, n, [], []
  # num_left = 3, num_right = 3, slate = [], result= []
  helper(num_left, num_right, slate, result)
  return result


if __name__ == '__main__':
  n = 3
  print(find_all_well_formed_brackets(n))