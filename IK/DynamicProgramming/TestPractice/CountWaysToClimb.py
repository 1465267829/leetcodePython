# # Complete the countWaysToClimb function below.
def countWaysToClimb(steps, n):
  memo = []
  steps_set = set(steps)
  for stair in range(n + 1):
    if stair == 0:
      memo.append(1)
      continue
    val = 0
    for step in steps:
      if stair - step >= 0:
        val += memo[stair - step]
    memo.append(val)
  return memo[-1]


if __name__ == '__main__':
  steps, n = [2, 3], 7
  print(countWaysToClimb(steps, n ))
