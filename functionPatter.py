
def patter (number:int):
    for i in range(number): #This row 
        for j in range(number-i-1,-1,-1) :
            print(j+1,end=" ")
        
    print()



number=int(input("enter number of row needed: "))
patter(number)
