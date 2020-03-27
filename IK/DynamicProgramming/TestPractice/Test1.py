"""

Recurrent equation:

F(n) = MAX(i * MAX(F(n-i), n-i) for all i in {1, 2, 3 .. n-1}


"""
def max_product_from_cut_pieces(n):
  table = [1] * (n+1)
  table[0] = 0
  table[1] = 1
  table[2] = 1

  for rope_length in range(3, len(table)):
    max_product_this_cut = 0
    for left_rope_length in range(1, rope_length):
      right_rope_length = rope_length - left_rope_length
      max_product_this_cut = max(max_product_this_cut, left_rope_length * max(table[right_rope_length],  right_rope_length)  )
    table[rope_length] = max_product_this_cut
  return table[-1]


if __name__ == '__main__':
  io = [[2, 1], [3, 2], [4, 4], [5, 6], [10, 36]]
  for input, exp_answer in io:
    answer = max_product_from_cut_pieces(input)
    print('ip = [{}] ans = [{}] expected answer [{}]'.format(input, answer, exp_answer))
    assert exp_answer == answer