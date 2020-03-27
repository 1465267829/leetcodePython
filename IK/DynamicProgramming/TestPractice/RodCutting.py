"""
This problem in CLRS is defined as following:

Page 360

15.1 Rod cutting

Our first example uses dynamic programming to solve a simple problem in deciding
where to cut steel rods. Serling Enterprises buys long steel rods and cuts them
into shorter rods, which it then sells. Each cut is free. The management of Serling
Enterprises wants to know the best way to cut up the rods.
We assume that we know, for i D 1;2; : : :, the price pi in dollars that Serling
Enterprises charges for a rod of length i inches. Rod lengths are always an integral
number of inches. Figure 15.1 gives a sample price table.
The rod-cutting problem is the following. Given a rod of length n inches and a
table of prices pi for i D 1;2; : : : ;n, determine the maximum revenue rn obtainable
by cutting up the rod and selling the pieces. Note that if the price pn for a rod
of length n is large enough, an optimal solution may require no cutting at all.


Read page 362 for the recurrent equation

Idea is:
We need to find "max price fetched by selling a rod of length rod_len by cutting it off
or selling intact"

Bottom Up approach is the following:
1.  We are given a price list for different lengths of the given rod.
    Remember they are off by 1, i.e 0th index value corresponds of price of rod of length 1
    Generally, ith index has price for rod of length i+1.

2.  Length of price list suggests the length of rod given.

3.  We brut force our way to find the max revenue by selling the cut rod.

4.  Following is what we do for a rod of given rod length :
    a.  We pretend to take the 1st cut at lengths 1 through length of rod.
        For example, for a rod of size 4 we pretend our 1st cuts to be:
        1. Rod of size 1
        2. Rod if size 2
        3. Rod of size 3
        4. Rod od size 4 [No cut, sell the rod as such]

        This is the outer loop

    b.  Each time we make a pretend 1st cut, we maximize our revenue with the leftover rod
        after the 1st cut.
        For example above:
        1. Maximize revenue for rod of size 3
        2. Maximize revenue for rod of size 2
        3. Maximize revenue for rod of size 1
        4. Maximize revenue for rod of size 0

        We know maximum revenue for rod of size 0 is 0 [$0]. This is our 'base' case.

        This is the inner loop

    c.  After we iterate through all the 1st cuts for a given rod length and follow the logic
        in 4a and 4b, we find the max revenue that we can get for the given rod length.

    d.  Here we notice at given the problem to find the max revenue for a rod length, depends
        on finding the max revenue for rod lengths smaller in size than the original length.
        For example:
        For rod length of 4, max of the following is the answer:
        1. (Price of 1st cut at length = 1) + (Max revenue fetched by rod of length 3)
        2. (Price of 1st cut at length = 2) + (Max revenue fetched by rod of length 2)
        3. (Price of 1st cut at length = 3) + (Max revenue fetched by rod of length 1)
        4. (Price of 1st cut at length = 4) + (Max revenue fetched by rod of length 0)

5.  Bottom up approach to solve this is to find out max revenue to be fetched for rod sized 0.
    Then for size 1 and 2 and 3 and finally for given size.

6.  In the code below max_price captures of max revenue to be generated for a given length of rod
    max_price[0] has the max revenue to be fetched if rod of length 0 with the given price list were to be given.
    max_price[1] has the max revenue to be fetched if rod of length 1 with the given price list were to be given.
    max_price[4] has the max revenue to be fetched if rod of length 4 with the given price list were to be given.

7.  curr_rod_len captures for what length we are are calculating the max obtainable revenue for.
    curr_rod_len varies from length of 1 to given length of rod

8.  curr_left_rod_len captures 1st cut length choices for given rod of length curr_rod_len.
    curr_left_rod_len varies from length 1 to curr_rod_len.

    For example for curr_rod_len 4:
    curr_left_rod_len = 3 indicates 1st cut being of length 3.

    Inner for loop brute forces through all the 1st cut lengths possible for curr_rod_len and stores the
    max revenue in max_so_far

    After calculating all the revenues for all the 1st cut choices it stores the max revenue in max_price at index
    curr_rod_len.
"""
import math


def cut_rod(prices):
  rod_len = len(prices)
  max_price = [0] * (len(prices)+1)

  for curr_rod_len in range(1, rod_len+1):
    max_so_far = -math.inf
    for curr_left_rod_len in range(1, curr_rod_len+1):
      max_so_far = max(max_so_far, prices[curr_left_rod_len-1] + max_price[curr_rod_len-curr_left_rod_len])
    max_price[curr_rod_len] = max_so_far
  return max_price[rod_len]


if __name__ == '__main__':
  prices = [1, 5, 8, 9, 10, 17, 17, 20]
  # prices = [1, 5, 8]
  print(cut_rod(prices))
