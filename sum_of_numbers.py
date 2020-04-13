def get_sum(a,b):
    '''
    Given two integers a and b, which can be positive or negative,
    find the sum of all the numbers between including them too and return it.
    If the two numbers are equal return a or b.
    Note: a and b are not ordered!
    :param a: int
    :param b: int
    :return: int
    '''
    if a == b:
        return a
    ab = [a, b]
    ab.sort()
    return sum(range(ab[0],ab[1]+1))

#testing
print(get_sum(0,1)) # ok
print(get_sum(4,4)) # ok
print(get_sum(0,-1))
print(get_sum(-2,0))
print(get_sum(-3,-2))
print(get_sum(4,2))
print(get_sum(-3,5))#ok
