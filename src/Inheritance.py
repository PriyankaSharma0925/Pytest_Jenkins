class ParentClass:
    parentNum=100

    def __init__(self,a,b):
        print("I am the constructor of Parent Class")
        self.firstNumber=a
        self.secondNumber=b

    def sum(self):
        return self.firstNumber + self.secondNumber + self.parentNum



##################################################Child Class###########################################3333

class ChildClass(ParentClass):
    def __init__(self,a,b):
        ParentClass.__init__(self,a,b)

    def completeSummation(self):
        return ParentClass.sum(self) + ParentClass.parentNum

    def sum(self,a,b):
        for b in a:
            print(f"{b} is present in {a}")

    def sum(self,a,b,c):
        return  super().sum()+a+b+c





obj= ChildClass(20,30)
print(obj.sum([2,4,6],6))
print(obj.completeSummation())
