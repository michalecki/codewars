import sys


def count_calls(func, *args, **kwargs):
    """Count calls in function func"""
    global i
    i = -1

    def fun_check(frame, event, arg):
        global i

        func(*args, **kwargs)
        if event == 'call':
            i += 1

    sys.settrace(fun_check)
    rv = func(*args, **kwargs)

    return i, rv


def add(a, b):
    return a + b


def add_ten(a):
    return add(a, 10)


def misc_fun():
    return add(add_ten(3), add_ten(9))


a = count_calls(add_ten, 5)
print(a)

# test.assert_equals(count_calls(add, 8, 12), (0, 20))
# test.assert_equals(count_calls(add_ten, 5), (1, 15))
# test.assert_equals(count_calls(misc_fun), (5, 32))
