def zero(a=0):
    if a == 0:
        return 0
    else:
        if a[0] == '+':
            return 0+ a[1]
        if a[0] == '-':
            return 0 - a[1]
        if a[0] == '*':
            return 0 * a[1]
        if a[0] == '//':
            return 0 // a[1]
def one(a=1):
    if a == 1:
        return 1
    else:
        if a[0] == '+':
            return 1+ a[1]
        if a[0] == '-':
            return 1 - a[1]
        if a[0] == '*':
            return 1 * a[1]
        if a[0] == '//':
            return 1 // a[1]
def two(a=2):
    if a == 2:
        return 2
    else:
        if a[0] == '+':
            return 2+ a[1]
        if a[0] == '-':
            return 2 - a[1]
        if a[0] == '*':
            return 2 * a[1]
        if a[0] == '//':
            return 2 // a[1]
def three(a=3):
    if a == 3:
        return 3
    else:
        if a[0] == '+':
            return 3+ a[1]
        if a[0] == '-':
            return 3 - a[1]
        if a[0] == '*':
            return 3 * a[1]
        if a[0] == '//':
            return 3 // a[1]
def four(a=4):
    if a == 4:
        return 4
    else:
        if a[0] == '+':
            return 4+ a[1]
        if a[0] == '-':
            return 4 - a[1]
        if a[0] == '*':
            return 4 * a[1]
        if a[0] == '//':
            return 4 // a[1]
def five(a=5):
    if a == 5:
        return 5
    else:
        if a[0] == '+':
            return 5+ a[1]
        if a[0] == '-':
            return 5 - a[1]
        if a[0] == '*':
            return 5 * a[1]
        if a[0] == '//':
            return 5 // a[1]
def six(a=6):
    if a == 6:
        return 6
    else:
        if a[0] == '+':
            return 6+ a[1]
        if a[0] == '-':
            return 6 - a[1]
        if a[0] == '*':
            return 6 * a[1]
        if a[0] == '//':
            return 6 // a[1]
def seven(a=7):
    if a == 7:
        return 7
    else:
        if a[0] == '+':
            return 7+ a[1]
        if a[0] == '-':
            return 7 - a[1]
        if a[0] == '*':
            return 7 * a[1]
        if a[0] == '//':
            return 7 // a[1]
def eight(a=8):
    if a == 8:
        return 8
    else:
        if a[0] == '+':
            return 8+ a[1]
        if a[0] == '-':
            return 8 - a[1]
        if a[0] == '*':
            return 8 * a[1]
        if a[0] == '//':
            return 8 // a[1]

def nine(a=9):
    if a == 9:
        return 9
    else:
        if a[0] == '+':
            return 9+ a[1]
        if a[0] == '-':
            return 9 - a[1]
        if a[0] == '*':
            return 9 * a[1]
        if a[0] == '//':
            return 9 // a[1]
def plus(digit):
    return '+', digit
def minus(digit):
    return '-', digit
def times(digit):
    return '*', digit
def divided_by(digit):
    return '//', digit

#testing

print(eight(plus(two())))
print(seven(minus(three())))
print(nine(times(five())))
print(zero(divided_by(zero())))