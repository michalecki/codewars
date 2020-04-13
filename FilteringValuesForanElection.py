import statistics
import math

def filter_val(lst):
    '''
    remove from the input list of integers the ones that are further from the mean than 2.5*pstdev
    :param lst:
    :return: input length, result length, mean, stdev/sqrt(length)
    '''
    # your code here
    len1 = len(lst)
    flag = True
    while flag:
        flag = False
        mean = statistics.mean(lst)
        sigma = statistics.pstdev(lst)
        low_bound = mean - 2.5 * sigma
        up_bound = mean + 2.5 * sigma
        for a in lst:
            if a > up_bound or a < low_bound :
                lst.remove(a)
                flag = True
    len2 = len(lst)
    s = sigma / math.sqrt(len2)
    return [[len1, len2], mean, s]

#test
a= [35, 34, 37, 32, 33, 36, 38, 32, 35, 35, 36, 34, 35, 100, 85, 70]
print(filter_val(a))