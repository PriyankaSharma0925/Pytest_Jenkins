class Basics:

    base_var = 20

    def __init__(self, a, b):
        print("I am the constructor")
        self.firstValue = a
        self.secondValue = b

    def basicFunc(self, a):
        new_value = a + self.firstValue + self.base_var
        Basics.base_var = new_value
        return new_value

    def basicDic(self, **kwargs):
        print(kwargs.items())
        print(kwargs)

    def base_varfun(self):
        print("Print Base Variable's new value")
        return self.base_var


obj = Basics(10, 20)
obj.basicFunc(100)
a = obj.base_varfun()
print(a)

# print(obj.basicDic(a=2,b=3,c=4,d=5))
