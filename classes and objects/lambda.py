fun=lambda a:a*10
print(fun(10))


def fun1(a,b=10,c='ram'):
    a.append('new one')
    b=100 # this won't change
    return a,b,c
li=[1,2,3] # this can be manipulated 
li1=20
print(fun1(li,li1))
print(li)
print(li1)
