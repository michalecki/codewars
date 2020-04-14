def solution(string,markers):
    '''
    Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
    Any whitespace at the end of the line should also be stripped out.
    Example:
    Given an input string of:

    apples, pears # and bananas
    grapes
    bananas !apples

    The output expected would be:

    apples, pears
    grapes
    bananas
    :param string:
    :param markers:
    :return: stripped string
    '''
    result=str()
    #splits the lines keeping the newlines
    lines = string.splitlines(keepends=True)

    for line in lines:
        #flag to mark the lines with the newline = all but last one
        if line.endswith('\n'): flag = True
        else: flag = False

        for marker in markers:
            if marker in line: line = line[:line.find(marker)]

        line = line.rstrip()
        result += line
        #adds the newline if the input had a newline
        if flag: result += '\n'

    return result

#testing
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

#better writen solution:
# parts = string.split('\n')
# for s in markers:
#     parts = [v.split(s)[0].rstrip() for v in parts]
# return '\n'.join(parts)