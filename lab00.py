
def ladder_of_numbers (number ):
    '''this function take a number then print it in descending order '''
    for n in number:
        print(n)
        n.split(n,n-1)
        while n!=0:
            n-=1
            print(n)
        print("/r")
        
    

ladder_of_numbers( 6 )
