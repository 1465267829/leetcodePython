def fact_recursive(n):
  if n == 0:
    return 1
  else:
    # Chip away at the probel by reducing it to size n-1
    # Ask worker clone to solve the smaller problem
    # Construct tyhe solution to the overall problem using that
    return n * fact_recursive(n-1)


def fact_iterative(n):
  result = 1 # fact(0) = 1
  for i in range(1, n+1): result *= i
  return result


if __name__ == '__main__':
  n = 5
  print(fact_recursive(n))
  print(fact_iterative(n))