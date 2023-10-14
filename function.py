def function_display(num:int) -> int :
    """This function take on parameters as integer number and reverse the parameter and print the output in list and decrese the number each time to give us the triangle shape.
    Note: Logical opreation here is to take number and subtract 1 form the given number to make the shape look. \n
    Like this:\n
    00000 \n
    0000 \n
    000 \n
    00 \n
    0 \n
    """
    
    for n in range(num,0,-1):
        for r in range(num,0,-1):
            print(r,end=" ")
        print()
        num -= 1
    return None

function_display(5)
print(function_display.__doc__)