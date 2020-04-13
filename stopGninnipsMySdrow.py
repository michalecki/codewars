def spin_words(sentence):
    '''
    Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

    Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"

    :param sentence: str
    :return: str
    '''
    words = sentence.split()
    result = str()
    # going through words of the sentence and spinning the ones longer than 5
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
        # adding the word and a space to the result string
        result += word + ' '

    # removing the trailing space
    result = result.rstrip()
    return result

#running some tests
print(spin_words('stop spinning my words'))
print(spin_words(''))
print(spin_words('very short test'))
print(spin_words('prestidigitator'))