def differentiate(equation, point):
    '''Create a function that differentiates a polynomial for a given value of x.
    Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate
    the equation as an integer.

    There will be a coefficient near each x, unless the coefficient equals 1 or -1.
    There will be an exponent near each x, unless the exponent equals 0 or 1.
    All exponents will be greater or equal to zero'''

    st = 0
    end = len(equation)
    result = 0
    # goes through the string calculating first derivative for each monomial and summing up
    while True:

        x_index = equation.find('x', st, end)
        if x_index == -1: break
        if x_index == 0:
            coef = 1
        else:
            try:
                coef = int(equation[st:x_index])
            except ValueError:
                # taking care of -1 and 1 coefficients
                if equation[st:x_index] == '-':
                    coef = -1
                elif equation[st:x_index] == '+':
                    coef = 1
                else:
                    break

        power = 1

        # print(x_index)
        # checks if 'x' is followed by an exponent
        try:
            if equation[x_index + 1] == '^':
                dig = x_index + 2
                # print(dig)
                # print(equation[dig])
                # checks if exponent consists of more than one digit
                try:
                    while equation[dig + 1].isdecimal():
                        # print(dig)
                        dig += 1
                except:
                    pass
                power = int(equation[x_index + 2:dig + 1])
                st = dig + 1
            else:
                st = x_index + 1

        except IndexError:
            st = x_index + 1

        temp_result = coef * power * point ** (power - 1)
        # print(coef, power, point)
        result += temp_result

    return result


# some testing

print(differentiate('34x^2-1', 4), 272)
print(differentiate('x^2', 59884848483559), 2 * 59884848483559)
print(differentiate('-7x^5+22x^4-55x^3-94x^2+87x-56', -3), -6045)
print(differentiate("x^2+3x+2", 3), 9)
print(differentiate("12x+2", 3), 12)
print(differentiate("x^2-x", 3), 5)
print(differentiate("-5x^2+10x+4", 3), -20)
print(differentiate("x^9-3x+4985", 2), 9 * 2 ** 8 - 3)
