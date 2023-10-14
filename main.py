def print_number (number:int):
    ''' This function print number from 5 to 1 '''

    for i in range(1,number):
        for j in range(i,number-1):
             print(f"{i}  ")
    print()         
   

numbers:int = 5
print_number(numbers)


# to docuement the function
print_number.__doc__
print(print_number.__doc__)


#another soluation
'''


'''
