def Subtract_Descending_Number(num:int) -> int :
    '''this function that takes 1 parameter of type int and make it in while loop that check if the number gretar than 0 
    it will be take it in for loop and in range start with this number and stop in 0 and 
    step one after that print that range in one line and make if conditional that check if the number is equal 0
    it will be break if not it will be the number -1 '''
    while num > 0:
        for n in range(num,0,-1): 
            print(n , end =" ")
        print(" ")
        if num == 0:
            #for n in range(a,0,-1): 
                #print(n , end =" ")
            break
        num -= 1     
number = int(input("please enter the number: "))
print(" ")    
Subtract_Descending_Number(number)
print(" ")
print(" ")
print(Subtract_Descending_Number.__doc__)