from random import randrange


def find_integer(arr):
    arr_set = set(arr)
    while True:
      random_number = randrange(0, 4000000000)
      if random_number not in arr_set: return random_number


if __name__ == '__main__':
  arr = [1,2]
  print(find_integer(arr))