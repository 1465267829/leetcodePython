# Complete the function below.
def helper(s, i, slate, result):
  # base
  if i == len(s):
    result.append(''.join(slate))
    return

  # recurse
  # exclude
  helper(s, i + 1, slate, result)
  # include
  slate.append(s[i])
  helper(s, i + 1, slate, result)
  slate.pop()
  return


def generate_all_subsets(s):
  s, i, slate, result = s, 0, [], []
  helper(s, i, slate, result)
  return result


if __name__ == '__main__':
  print(generate_all_subsets('a'))