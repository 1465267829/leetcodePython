def pow_recursive(n, k):
  # Here we chjp the problem by 1 unit at a time
  if k == 0:
    return 1
  else:
    return n * pow_recursive(n, k-1)


def pow_iterative(n, k):
  result = 1
  for i in range(1, k+1): result *= n
  return result


if __name__ == '__main__':
  n, k = 5, 4
  print(pow_recursive(n, k))
  print(pow_iterative(n, k))