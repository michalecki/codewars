class RomanNumerals:
    '''
    converts roman numerals in arabic decimal and vice versa
    '''

    def __init__(self):
        self.number = int()

    def to_roman(self, number):
        self.number = number
        roman_number = str()
        while self.number > 0:
            roman_number += self.get_roman(self.number)
        return roman_number

    def get_roman(self, number):
        if number - 1000 >= 0:
            self.number -= 1000
            return 'M'
        if number - 900 >= 0:
            self.number -= 900
            return 'CM'
        if number - 500 >= 0:
            self.number -= 500
            return 'D'
        if number - 400 >= 0:
            self.number -= 400
            return 'CD'
        if number - 100 >= 0:
            self.number -= 100
            return 'C'
        if number - 90 >= 0:
            self.number -= 90
            return 'XC'
        if number - 50 >= 0:
            self.number -= 50
            return 'L'
        if number - 40 >= 0:
            self.number -= 40
            return 'XL'
        if number - 10 >= 0:
            self.number -= 10
            return 'X'
        if number - 9 >= 0:
            self.number -= 9
            return 'IX'
        if number - 5 >= 0:
            self.number -= 5
            return 'V'
        if number - 4 >= 0:
            self.number -= 4
            return 'IV'
        if number - 1 >= 0:
            self.number -= 1
            return 'I'

    def from_roman(self, roman_number):
        numbers = []
        arabic = 0
        for letter in reversed(roman_number):
            numbers.append(self.roman_values(letter))
        for i in range(len(numbers)):
            arabic += numbers[i]
            try:
                if numbers[i] > numbers[i + 1]:
                    arabic -= numbers[i + 1] * 2
            except IndexError:
                pass

        return arabic

    def roman_values(self, numeral):
        if numeral == 'I':
            return 1
        if numeral == 'V':
            return 5
        if numeral == 'X':
            return 10
        if numeral == 'L':
            return 50
        if numeral == 'C':
            return 100
        if numeral == 'D':
            return 500
        if numeral == 'M':
            return 1000


RomanNumerals = RomanNumerals()

print(RomanNumerals.from_roman('MDCCLXXIV'))

print(RomanNumerals.to_roman(2477))
print(RomanNumerals.to_roman(1543))
print(RomanNumerals.to_roman(1999))
