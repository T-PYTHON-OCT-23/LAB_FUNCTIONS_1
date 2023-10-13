def My_functhon(n):
    '''It prints a pattern in decreasing order from n to 1'''
    for i in range(n, 0, -1):
        print(" ".join(str(j) for j in range(i, 0, -1)))

My_functhon(5)

print(My_functhon.__doc__)