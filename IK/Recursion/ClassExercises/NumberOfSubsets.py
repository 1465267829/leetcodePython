def subsets_recusive(n):
  if n == 0:
    return 1
  else:
    return 2 * subsets_recusive(n-1)


def subsets_iterative(n):
  result = 1
  for i in range(1, n+1):
    result *= 2
  return result


if __name__ == '__main__':
  print(subsets_recusive(7))
  print(subsets_iterative(7))