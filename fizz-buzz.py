#!/usr/bin/env python

def checkio(number):
    if not number % 15:
        number = 'Fizz Buzz'
    elif not number % 5:
        number = 'Buzz'
    elif not number % 3:
        number = 'Fizz'
    else:
        number = str(number)
 
    return str(number)

#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
