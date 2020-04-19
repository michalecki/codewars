def exp_sum(n):
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
    :param n: int
    :return: integer partition, int
    '''

#solution works but fails on time
    # partition = int()
    # if n == 1: return 1
    # if n == 0: return 1
    # if n<0 : return 0
    # k=1
    # count=0
    #
    # krange = ((24*n+1)**(1/2)+1)/6
# #recurrent formula from wikipedia
    # while  -krange <= k <= krange:
    #
    #     if count % 2 == 1:
    #         k *= -1
    #
    #     partition += (-1)**(k+1)*exp_sum(n-k*(3*k-1)/2)
    #
    #     if count % 2 == 1:
    #         k = -k+1
    #     count += 1
    #
    # return partition

    if -krange <= k <= krange:
        if count % 2 == 1:
            k *= -1

        partition += (-1)**(k+1)*exp_sum(n-k*(3*k-1)/2)

        if count % 2 == 1:
            k = -k+1
        count += 1

# testing
# exp_sum(5)
print(exp_sum(6))