import math as mt
class Equation:
    def __init__(self,a,b,c):   #定义类的基础属性——三个变量
        self.a = a
        self.b = b
        self.c = c
    def getDiscriminant(self):  #计算Δ的构造函数
        self.delta = self.b ** 2 - 4 * self.a * self.c
        return self.delta
    def getRoot(self):  #分类别进行讨论，Δ<0无实数解，Δ>=0时利用公式法求解
        if self.delta < 0:
            return print(None)
        else:
            root1 = (-self.b+mt.sqrt(self.delta))/2*self.a
            root2 = (-self.b-mt.sqrt(self.delta))/2*self.a
            return print("Root1={},Root2={}".format(root1,root2))
if __name__ == '__main__':
    a = float(input("输入变量a:"))
    b = float(input("输入变量b:"))
    c = float(input("输入变量c:"))
    Eq = Equation(a,b,c)    #实例化类Equation为新建对象Eq
    Eq.getDiscriminant()    #对象访问Δ函数
    Eq.getRoot()    #对象访问求根函数
