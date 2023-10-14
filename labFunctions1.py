def function1(n):
    '''
this function that takes 1 parameter of type int,
then it prints out the result 
formatted like the following patter 
(if we give it 5 for example):
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1'''

    number:int = n
    for val in range(0, n):
        val=n
        while val!=0:    
            print(val,end=" ")
            val-=1
        else:
            print()
        n-=1

function1(5)

print(function1.__doc__)