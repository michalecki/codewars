def tickets(people):
    '''
    The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line.
     Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
    Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
    Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

    Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
    :param people: list of int
    :return: str YES or NO
    '''

    stock = {25: 0, 50: 0, 100: 0}
    count = 0
    while True:

        if people[count] == 25:
            stock[25] += 1

        elif people[count] == 50:
            if stock[25] < 1:
                return "NO"
            else:
                stock[25] -= 1
                stock[50] +=1

        elif people[count] == 100:
            if stock[50] < 1 :
                if stock[25] < 3:
                    return "NO"
                elif stock[25] >= 3:
                    stock[25] -= 3
                    stock[100] += 1

            if stock[50] >= 1:
                if stock[25] < 1:
                    return "NO"
                elif stock[25] >= 1:
                    stock[50] -= 1
                    stock[25] -= 1
                    stock[100] += 1
        else: break
        count += 1
        if count >= len(people):
            return 'YES'


#testing
print(tickets([25,50,25,25,25,50,100,50,25,100]))