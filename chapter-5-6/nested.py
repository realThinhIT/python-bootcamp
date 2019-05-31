import copy

listOfLists = [
    [0, 'hello'],
    [1, 'hi'],
    [2, 'how are you']
]

greetings = [item[1] for item in listOfLists]
print(greetings)

nestedNumbers = [
    [0, 1, 2, 3, 4],
    [5, 6, 7],
    [8, 9],
    [10]
]

flattened = [number for list in nestedNumbers for number in list]
print(flattened)

newNumbers2 = copy.deepcopy(nestedNumbers)
newNumbers2[0][0] = 1000
print(newNumbers2)
print(nestedNumbers)

newNumbers = nestedNumbers.copy()
newNumbers[0][0] = 1000
print(nestedNumbers)

powerOfTwo = [x**2 for list in nestedNumbers for x in list]
print(powerOfTwo)