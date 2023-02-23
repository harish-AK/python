def fun(n):
    if n==0:
        print("complete")
    else:
        print(fun(n-1))
fun(5)