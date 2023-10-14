def pattern (p:int):
    """I use pattern function to creat pattern by using for loop"""
    print(pattern.__doc__,"\n")
    pattern.__doc__
    for row in range (p,0,-1):
        for column in range(row,0,-1):
            print(column,end=" ")
        

        print('')      
p=5
pattern(p)



'''
def pattern (p:int):
    #p=int(input("enter the number :"))
    for row in range (0,p):
        for column in range(p,row,-1):
            print(p,end=" ")

        print('')
p=6       
pattern(p)
'''

'''
def pattern (p:int):
    #p=int(input("enter the number :"))
    for row in range (p,0,-1):
        for column in range(1,row,+1):
            print(column,end=" ")
        

        print('')
p=6      
pattern(p)
'''





