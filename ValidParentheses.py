def valid_parentheses(string):
    '''
    Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
    The function should return true if the string is valid, and false if it's invalid.
    Examples

    "()"              =>  true
    ")(()))"          =>  false
    "("               =>  false
    "(())((()())())"  =>  true

    Constraints

    0 <= input.length <= 100

    Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
    Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms
    of brackets as parentheses (e.g. [], {}, <>).

    :param string:
    :return: True/False
    '''
    if len(string) > 100:
        return print('input error')
    control = 0
    for letter in string:
        if letter == '(':
            control += 1
        elif letter == ')':
            control -= 1
        if control < 0:
            return False
    if control == 0:
        return True
    else: return False


#testing

print(valid_parentheses(' (dupa))'))