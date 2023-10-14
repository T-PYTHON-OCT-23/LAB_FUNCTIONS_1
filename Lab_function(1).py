#lab function (1)
def decremental_func(value:int):
    ''' The function prints in a triangular shape using a decremental method.'''
    for num in range(0,value-1,1):#for loop 
         for num1 in range(value-num,0,-1):#nested for loop 
            print(num1,end=" ")
         print()
          
value = int(input('Enter a value:'))
decremental_func(value)
print(decremental_func.__doc__)#Documentation