
class Basics:

    base_var=20

    def __init__(self, a,b):
        print("I am the constructor")
        self.firstValue= a
        self.secondValue= b

    def basicFunc(self, a):
        new_value=a+ self.firstValue + self.base_var
        return new_value



obj=Basics(10,20)
print(obj.basicFunc(10))
