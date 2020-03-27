"""
Top K



Problem Statement:



You are given an array of integers arr, of size n, which is analogous to a continuous stream of integers input. Your task is to find K largest elements from a given stream of numbers.

By definition, we don't know the size of the input stream. Hence, produce K largest elements seen so far, at any given time. For repeated numbers, return them only once.



If there are less than K distinct elements in arr, return all of them.



Note:

Don't rely on size of input array arr.
Feel free to use built-in functions if you need a specific data-structure.


Input/Output Format For The Function:



Input Format:



There is only one argument: Integer array arr.



Output Format:



Return an integer array res, containing K largest elements. If there are less than K unique elements, return all of them.

Order of elements in res does not matter.



Input/Output Format For The Custom Input:



Input Format:



The first line of input should contain an integer n, denoting size of input array arr. In next n lines, ith line should contain an integer arr[i], denoting a value at index i of arr.

In the next line, there should be an integer, denoting value of K.



If n = 5, arr = [1, 5, 4, 4, 2] and K = 2, then input should be:



5

1

5

4

4

2

2



Output Format:



Let’s denote size of res as m, where res is the array of integers returned by solution function.

Then, there will be m lines of output, where ith line contains an integer res[i], denoting value at index i of res.



For input n = 5, arr = [1, 5, 4, 4, 2] and K = 2, output will be:



4

5



Constraints:

1 <= n <= 10^5
1 <= K <= 10^5
arr may contains duplicate numbers.
arr may or may not be sorted


Sample Test Case:



Sample Test Case 1:



Sample Input 1:



arr = [1, 5, 4, 4, 2]; K = 2



Sample Output 1:



[4, 5]



Sample Test Case 2:



Sample Input 2:



arr = [1, 5, 1, 5, 1]; K = 3



Sample Output 2:



[5, 1]
"""
import heapq

# def topK(arr, k):
#   min_heap = []
#   max_heap = []
#   for i in range(k):heapq.heappush(min_heap, arr[i])
#
#   for i in range(k, len(arr)):
#     if arr[i] == min_heap[0]:
#       if len(min_heap) < k:
#         heapq.heappush(min_heap, arr[i])
#       else:
#         heapq.heappush(max_heap, (-1) * arr[i])
#     elif arr[i] < min_heap[0]:
#       heapq.heappush(max_heap, (-1) * arr[i])
#     else:
#       heapq.heappush(min_heap, arr[i])
#       if len(min_heap) > k:
#         item = heapq.heappop(min_heap)
#         heapq.heappush(max_heap, (-1) * item)
#
#   temp = set()
#   while len(temp) < k:
#     if min_heap:
#       temp.add(heapq.heappop(min_heap))
#     elif max_heap:
#       temp.add((-1) * heapq.heappop(max_heap))
#     else:
#       break
#   result = list(temp)
#   return result

def topK(arr, k):
  max_heap = []
  for element in arr: heapq.heappush(max_heap, (-1) * element)
  result = []
  while len(result) < k and max_heap:
    value = (-1) * heapq.heappop(max_heap)
    if not result:
      result.append(value)
      continue
    if value != result[len(result)-1]: result.append(value)
  return result


if __name__ == '__main__':
  # arr, k = [1, 5, 4, 4, 2], 2
  # arr, k = [1, 5, 1, 5, 1], 3
  # arr, k = [5,6,1,4,1,8,2,4,1,7,9,3,2,1], 2
  # arr, k = [4,8,9,6,6,2,10,2,8,1,2], 9
  # arr, k = [4,1,8,1,9,10,3,9,4,4,2,5,7,1,3,5], 8
  arr, k = [5,4,3,5,6,6,9,2,5,1,1,6,9,5,10,5,5,10],15

  print(topK(arr, k))
  # topK(arr, k)