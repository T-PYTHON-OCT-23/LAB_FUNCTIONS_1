

def numerical_sequence(num:int):
    """
Print numbers in reverse sequence from the same number to number one.
    """
    
    for n in range(num,0,-1):
        for i in range(n,0,-1):

            print(i,end=' ')
        
        print()
        

numerical_sequence(5)

print(numerical_sequence.__doc__)

