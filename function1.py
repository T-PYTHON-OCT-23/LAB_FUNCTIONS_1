# Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

# Document the newly created function. describe what it does, then print the documentation. 

def number (num):
    if num < 1:
        return

    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()

n = 5
number(n) 




