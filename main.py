ans = int(input("Enter a number: "))

for i in range(ans,0,-1):
    list_= []
    for j in range(i,0,-1):
        list_.append(j)
    print(list_)
    
doc="""take a number from user and print the pattern
each line should be a list
and i use nested for loop 
one for the pattern and the other for each list
"""
print(doc)