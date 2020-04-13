import math
def prob_simpson(lamb, x, op='='):
    '''

    :param lamb: average value
    :param x: desired value
    :param op: '=' (default) prob. of desired value
    > cumulative probability of values lower than desired >= or lower or equal
    < and <= as above, higher
    :return: probability
    '''
    #your code here
    def prob_funct(lamb, x):
        return lamb**x*math.e**(-lamb)/math.factorial(x)
    cum_prob = float()
    if op == '=':
        return prob_funct(lamb,x)
    if op == '>' or op == '<=':
        for i in range(x):
            cum_prob += prob_funct(lamb, i)
        if op == '>':
            return cum_prob
        else:
            return 1 - cum_prob
    if op == '>=' or op =='<':
        for i in range(x+1):
            cum_prob += prob_funct(lamb, i)
        if op == '>=' :
            return cum_prob
        else:
            return 1-cum_prob


#testing

print(prob_simpson(8,12,'>='))

#
# And an ellegant solution:

# from math import e, factorial
# poi = lambda l,x: e**-l*l**x/factorial(x)
#
# def prob_simpson(l, x, op='='):
#     if op == '=': return poi(l,x)
#     if op == '>=': return sum(poi(l,e) for e in range(x+1))
#     if op == '>': return sum(poi(l,e) for e in range(x))
#     if op == '<=': return 1-sum(poi(l,e) for e in range(x))
#     if op == '<': return 1-sum(poi(l,e) for e in range(x+1))