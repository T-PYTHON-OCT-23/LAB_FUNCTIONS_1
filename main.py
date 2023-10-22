n=int(input("Enter the number :"))

def t_pattern(n:int):
    output=''
    for row in range(n,0,-1):
        for col in range(row,0,-1):
            output+= f"{col}"
        output += "\n"
            #print(col,end='')
    return output
      
pattern =t_pattern(n)
print(pattern)