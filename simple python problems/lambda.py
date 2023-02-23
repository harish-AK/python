x=lambda a:a+10      # a is like return statement
print(x(10))

y=lambda a,b:a*b
print(y(2,3))


def lam(n):
    return lambda a: a*n
var=lam(10)
print(var(10))