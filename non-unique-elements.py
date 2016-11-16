def checkio(data):

# Here's one way to do it.
#    duplicates = []
#    for item in data:
#        if data.count(item) > 1:
#            duplicates.append(item)    
#    return duplicates

# Here it is in a one liner :-)
    return [item for item in data if data.count(item) > 1]

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
