def make_readable(seconds):
    '''
    Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

    :param seconds:
    :return:
    '''

    s = seconds % 60
    h = seconds // 3600
    m = seconds // 60 - h*60

#f-strings
    return f"{h:02d}:{m:02d}:{s:02d}"


    #testing


print(make_readable(60))
print(make_readable(5100))
print(make_readable(10000))