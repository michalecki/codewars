def duplicate_encode(word):
    '''
    The goal of this exercise is to convert a string to a new string where each character in the new string
    is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
    Ignore capitalization when determining if a character is a duplicate.
    :param word: str
    :return: str
    '''
    word = word.lower()

    #nice normal writing
    # result = str()
    # for letter in word:
    #     if word.count(letter) > 1:
    #         result += ')'
    #     else:
    #         result +='('
    # return result

#one liner
    #In general,
    # [f(x) if condition else g(x) for x in sequence]
    # And, for list comprehensions with if conditions only,
    # [f(x) for x in sequence if condition]
#word can be substituted with word.lower() for a true one-liner
    return ''.join([')' if word.count(n) > 1 else '(' for n in word])

#testing
print(duplicate_encode('dupa'))
print(duplicate_encode('adupa'))
print(duplicate_encode('Dupamama'))
print(duplicate_encode('Duzuda'))