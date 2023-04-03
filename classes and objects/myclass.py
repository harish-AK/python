class mine():
    con=10
    def __init__(self):
        self.a=30
    def fun(self,q,q1): # fun function has 2 arguments so we need to pass 2 parameters during the function call.
        return self.a
c=mine()
print(c.fun(1,1))