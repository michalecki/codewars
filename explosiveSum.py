def exp_sum(n,memo = {}):
    '''
    From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

    In number theory and combinatorics, a partition of a positive integer n, also called an integer partition,
    is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are
    considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned
    in five distinct ways:

    4
    3 + 1
    2 + 2
    2 + 1 + 1
    1 + 1 + 1 + 1
    :param memo: saving the already calculated value
    :param n: int
    :return: integer partition, int
    '''


    partition = int()
    if n == 1: return 1
    if n == 0: return 1
    if n<0 : return 0
#adding the dictionary keeping the calculated values
#use it if already calculated
    try:
        return memo[n]
    except KeyError:

        k=1
        count=0

        krange = ((24*n+1)**(1/2)+1)/6
    #recurrent formula from wikipedia
        while  -krange <= k <= krange:

            if count % 2 == 1:
                k *= -1

            partition += (-1)**(k+1)*exp_sum(n-k*(3*k-1)/2)

            if count % 2 == 1:
                k = -k+1
            count += 1
        memo[n] = partition
        return partition

# #some more clever and neat solution
# def exp_sum(n):
#   if n < 0:
#     return 0
#   dp = [1]+[0]*n
#   # print(dp)
#   for num in range(1,n+1):
#     for i in range(num,n+1):
#       dp[i] += dp[i-num]
#       # print(dp)
#   return dp[-1]

# testing
# exp_sum(5)
print(exp_sum(5))