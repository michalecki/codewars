def digital_root(n):
    '''
    A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n.
    If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
    This is only applicable to the natural numbers.
    :param n: positive int 
    :return: int
    '''
    #little helper function
    def sums_digits(n):
        digits = str(n)
        sum=0
        for digit in digits:
            sum += int(digit)
        return sum
    while n >= 10:
        n = sums_digits(n)
    return n

#better solution
    #map(function,iterable) applies a function to each iterable
    return n if n < 10 else digital_root(sum(map(int, str(n))))


#some testing



print(digital_root(0))
print(digital_root(5))
print(digital_root(15))
print(digital_root(355))