def printFunction(number):
    """
    This function receives an integer number and print it as a list that decrements to 1
    Example:
    4321
    321
    21
    1
   """
    for num in range(number, 0 , -1):
        for n in range(num, 0, -1):
            print(n, end=' ')
       
        print("\n")


printFunction(5)
print(printFunction.__doc__)