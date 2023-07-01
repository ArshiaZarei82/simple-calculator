def Addition(listOfNumbers):
    numbersAddition = 0
    for x in range(len(listOfNumbers)):
        numbersAddition += listOfNumbers[x]
    return numbersAddition


def Subtraction(listOfNumbers):
    numbersSubtraction = listOfNumbers[0]
    for x in range(1, len(listOfNumbers)):
        numbersSubtraction -= listOfNumbers[x]
    return numbersSubtraction


def Division(listOfNumbers):
    numbersDivision = listOfNumbers[0]
    for x in range(1, len(listOfNumbers)):
        numbersDivision /= listOfNumbers[x]
    return numbersDivision


def Multiplication(listOfNumbers):
    numbersMultiplication = 1
    for x in range(len(listOfNumbers)):
        numbersMultiplication *= listOfNumbers[x]
    return numbersMultiplication