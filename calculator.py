# Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces
# returns the value of that expression
#
# Example:
# Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
#
# Remember about the order of operations! Multiplications and divisions have a higher priority and should be
# performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.


import re

class Calculator:

    def evaluate(self,string):
        #re to find the operators
        self.char_list = re.split('([*/+\-()])', string)
        #removing empty items from the list
        while '' in self.char_list:
            del self.char_list[self.char_list.index('')]
        while ' ' in self.char_list:
            del self.char_list[self.char_list.index(' ')]

        #if the expression starts with a negative number
        if self.char_list[0] == '-':
            self.char_list[1] = str(float(self.char_list[1]) * -1)
            del self.char_list[0]

        #removing whitespaces and converting numbers to floats
        for i in range(len(self.char_list)):
            self.char_list[i].strip()

            try:
                self.char_list[i]= float(self.char_list[i])
            except:
                pass


        while len(self.char_list) > 1:
            l=1
            #brackets first
            Calculator.bracket(self)

            #multiplying and dividing
            while l != len(self.char_list):
                l=len(self.char_list)
                Calculator.multiplDivide(self)

            l=1
            #adding and subtracting
            while l != len(self.char_list):
                l = len(self.char_list)
                Calculator.addsubstract(self)
        return self.char_list[0]

    def bracket(self):
        #finding the brackets
        while ')' in self.char_list:
            try:
                b = self.char_list.index(')')
                a = self.char_list.index('(')

                while '(' in self.char_list[a+1:b+1]:
                    a = self.char_list.index('(',a+1)
                del self.char_list[b]
                del self.char_list[a]
            except:
                "ValueError"
            #if expression in brackets starts with a negative number
            if self.char_list[a] == '-':
                self.char_list[a+1] *= -1
                del self.char_list[a]
                b += -1

            Calculator.multiplDivide(self,a,b-1)
            Calculator.addsubstract(self,a,b-1)


    def multiplDivide(self,a=0,b=-1):
        while '*' in self.char_list[a:b] or '/' in self.char_list[a:b]:
            #multiply and divide from left to right
            try:
                if self.char_list.index('*',a) < self.char_list.index('/',a):
                    try:
                        i = self.char_list.index('*', a)
                        self.char_list[i - 1:i + 2] = [self.char_list[i - 1] * self.char_list[i + 1]]
                        if b != -1: b += -3
                        continue
                    except ValueError:
                        pass
                elif self.char_list.index('*',a) > self.char_list.index('/',a):
                    try:
                        i = self.char_list.index('/', a)
                        self.char_list[i - 1:i + 2] = [self.char_list[i - 1] / self.char_list[i + 1]]
                        if b != -1: b += -3
                        continue
                    except ValueError:
                        pass
            except:
                try:
                    i = self.char_list.index('/', a)
                    self.char_list[i - 1:i + 2] = [self.char_list[i - 1] / self.char_list[i + 1]]
                    if b != -1: b += -3
                except ValueError:
                    pass
                try:
                    i = self.char_list.index('*', a)
                    self.char_list[i - 1:i + 2] = [self.char_list[i - 1] * self.char_list[i + 1]]
                    if b != -1: b += -3
                except ValueError:
                    pass


    def addsubstract(self,a=0,b=-1):
        while '+' in self.char_list[a:b] or '-' in self.char_list[a:b]:
#add and subtract from left to right
            try:
                if self.char_list.index('+',a) < self.char_list.index('-',a):
                    try:
                        i = self.char_list.index('+', a)
                        self.char_list[i - 1:i + 2] = [self.char_list[i - 1] + self.char_list[i + 1]]
                        if b != -1: b += -3
                        continue
                    except ValueError:
                        pass
                elif self.char_list.index('+',a) > self.char_list.index('-',a):
                    try:
                        i = self.char_list.index('-', a)
                        self.char_list[i - 1:i + 2] = [self.char_list[i - 1] - self.char_list[i + 1]]
                        if b != -1: b += -3
                        continue
                    except ValueError:
                        pass
            except:
                try:
                    i = self.char_list.index('-', a)
                    self.char_list[i - 1:i + 2] = [self.char_list[i - 1] - self.char_list[i + 1]]
                    if b != -1: b += -3
                except ValueError:
                    pass
                try:
                    i = self.char_list.index('+', a)
                    self.char_list[i - 1:i + 2] = [self.char_list[i - 1] + self.char_list[i + 1]]
                    if b != -1: b += -3
                except ValueError:
                    pass



