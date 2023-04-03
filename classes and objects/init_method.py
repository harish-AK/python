class mouth():
    def __init__(self,age,name):
        self.age=age   # properties declared using init method 
        self.name=name
    def fun(self):
        print(f"age is  {self.age}, name is {self.name}")
p=mouth(12,'ramu')
p.fun()