def fun(n):
    '''طباعة الارقام بشكل عكسي_هرمي'''
    for i in range(n, 1, -1):
        if i == 0:
         continue
        print(*range(i))
fun(6) 