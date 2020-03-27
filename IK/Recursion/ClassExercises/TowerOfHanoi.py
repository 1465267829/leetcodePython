# def tower_of_hanoi(n, src, dst, aux):
#   if n == 1:
#     print('Move {} disk from {} to {}'.format(n, src, dst))
#     return
#   tower_of_hanoi(n-1, src, aux, dst)
#   print('Move {} disk from {} to {}'.format(n, src, dst))
#   tower_of_hanoi(n-1, aux, dst, src)
#
#
# if __name__ == '__main__':
#   n = 3
#   tower_of_hanoi(n, '''"A"''', '''"B"''', '''"C"''')


# def tower_of_hanoi(n):
#   def helper(n, src, dst, aux):
#     if n == 1:
#       result.append([src, dst])
#       return
#     helper(n - 1, src, aux, dst)
#     result.append([src, dst])
#     helper(n - 1, aux, dst, src)
#
#   result = []
#   helper(n, 1, 2, 3)
#   return result

def tower_of_hanoi(n):
  def helper(n, src, aux, dst):
    if n == 1:
      result.append([src, dst])
      return
    helper(n - 1, src, dst, aux)
    result.append([src, dst])
    helper(n - 1, aux, src, dst)

  result = []
  helper(n, 1, 2, 3)
  return result

if __name__ == '__main__':
  n = 4
  print(tower_of_hanoi(n))