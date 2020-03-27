def fibonnaci_recursive(n):
  if n == 0 or n == 1:
    return n
  else:
    return fibonnaci_recursive(n-1) + fibonnaci_recursive(n-2)


def fibonnaci_iterative(n):
  n_2, n_1, result = 0, 1, None
  for _ in range(2, n+1):
    result = n_2 + n_1
    n_2 = n_1
    n_1 = result
  return result


if __name__ == '__main__':
  print(fibonnaci_recursive(7))
  print(fibonnaci_iterative(7))