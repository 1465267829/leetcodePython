'''
Explains three ways to generate permutations with repetition
and chooses DFS and sticks with it
'''

# enumerate all possible binary strings

def binary_strings_recursive_right_to_left(n):
  # BFS
  # generating string right to left
  # top heavy, root does most work
  # allocate exponential amount of space
  # in last iterations
  if n == 1:
    return ['0', '1']

  prev = binary_strings_recursive_right_to_left(n - 1)
  result = []
  for i in prev:
    result.append(i + '0')
    result.append(i + '1')
  return result


def binary_strings_iterative_right_to_left(n):
  # BFS
  # allocate exponential amount of space
  # in last iterations
  result = ['0', '1']
  for i in range(2, n+1):
    new_result = []
    for item in result:
      new_result.append(item + '0')
      new_result.append(item + '1')
    result = new_result
  return result


def binary_strings_recursive_left_to_right(n):
  def helper(slate, n):
    # DFS
    # generating string left to right
    # every node other than leaf level does constant work
    # bottom heavy, leaf does most work
    if n == 0:
      result.append(slate)
    else:
      helper(slate + '0', n-1)
      helper(slate + '1', n-1)

  result = []
  helper('', n)
  return result


if __name__ == '__main__':
  n = 3
  print(binary_strings_recursive_right_to_left(n))
  print(binary_strings_iterative_right_to_left(n))
  print(binary_strings_recursive_left_to_right(n))
