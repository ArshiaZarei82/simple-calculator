import functions
while True:
    numberOfOperands = int(input("How many numbers do you have :"))
    operator = input("What operation do you want?\n please enter *, /,-,+ :")


    listOfNumbers = []
    for x in range(int(numberOfOperands)):
        listOfNumbers.append(int(input("Enter your number :")))
    # print(listOfNumbers)

    if operator == "+":
        print("your answer is :", functions.Addition(listOfNumbers))
    elif operator == "-":
        print("your answer is :", functions.Subtraction(listOfNumbers))
    elif operator == "/":
        print("your answer is :", functions.Division(listOfNumbers))
    elif operator == "*":
        print("your answer is :", functions.Multiplication(listOfNumbers))

    choice = input("do you want to continue? 'yes' or 'no': ")
    if choice == 'yes':
        continue
    else:
        print("see you later")
        break