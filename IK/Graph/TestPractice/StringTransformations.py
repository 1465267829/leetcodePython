from string import ascii_lowercase


def string_transformation(words, start, stop):
  def discover_neighbors(self, word):
    neighbors = []
    for i in range(len(word)):
      temp = list(word)
      for alpha in ascii_lowercase:
        temp[i] = alpha
        if tuple(temp) in words:
          neighbors.append(tuple(temp))
          words.remove(tuple(temp))
    return neighbors

  words = set()
  for word in words:
    words.add(tuple([word[i] for i in range(len(word))]))

  bword = tuple([start[i] for i in range(len(start))])
  eword = tuple([stop[i] for i in range(len(stop))])

  num_transform = 0
  q = [bword]
  while q:
    num_transform += 1
    for _ in range(len(q)):
      curr = q.pop(0)
      if curr == eword:
        return num_transform
      for n in discover_neighbors(curr):
        q.append(n)
    pass  # while
  return ['-1']


if __name__ == '__main__':
  n, words, start, stop = 4, ["cat", "hat", "bad", "had"], "bat", "had"
  # n, words, start, stop = 4, [], "bat", "had"
  # n, words, start, stop = 4,  ["cccw", "accc", "accw"], "cccc", "cccc"
  print(string_transformation(words, start, stop))


