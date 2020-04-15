import string
def pig_it(text):
    '''
    Move the first letter of each word to the end of it, then add "ay" to the end of the word.
    Leave punctuation marks untouched.
    :param text:
    :return: modified text
    '''
#string.punctuation lists the punctuation marks
    return ' '.join(word[1:] + word[0] + 'ay' if word not in string.punctuation else word for word in text.split())


#testing

print(pig_it('Pig latin is cool'))
print('igPay atinlay siay oolcay')
print(pig_it('Hello world !'))
print('elloHay orldway !')