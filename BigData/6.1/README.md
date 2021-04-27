### Python：用类与对象写一元二次方程计算器中遇到的错误



练习题：为二次方程式$y=ax^2+bx+c$设计一个名为Equation的类，这个类包括：

1）代表3个系数的成员变量a、b、c；

2）一个参数为a、b、c的构造方法；

3）一个名为getDiscriminant()的方法返回判别式的值；

4）两个分别名为getRoot1()和getRoot2()的方法返回方程的两个根，如果判别式为负，这些方法返回None。

#### 过程分析：

利用公式法求解，其中： $\Delta = b^2-4ac$

$\Delta$ > 0 时，
$$
Root =\frac{-b\pm\sqrt\Delta}{2a}
$$
$\Delta $< 0 时，
$$
Root =\frac{-b\pm\sqrt{4ac-b^2}i}{2a}
$$
$\Delta$=0时,
$$
Root = -\frac{b}{2a}
$$
数学分析完毕，实现代码如下：

```python
import math as mt

class Equation:
    def __init__(self,a,b,c):   #定义类的基础属性——三个变量
        self.a = a
        self.b = b
        self.c = c
    def getDiscriminant(self):  #计算Δ的构造函数
        self.delta = self.b ** 2 - 4 * self.a * self.c
        return self.delta
    def getRoot1(self):
        if self.delta < 0:
            return None
        else:
        	return (-self.b + math.sqrt(self.getDiscriminant())) / (2 * self.a)
    def getRoot2(self):
        if self.delta < 0:
            return None
        else:
        	return (-self.b - math.sqrt(self.getDiscriminant())) / (2 * self.a)
    
if __name__ == '__main__':
    a = float(input("输入变量a:"))
    b = float(input("输入变量b:"))
    c = float(input("输入变量c:"))
    Eq = Equation(a,b,c)    #实例化类Equation为新建对象Eq
    Eq.getDiscriminant()    #对象访问Δ函数
    Eq.getRoot()    #对象访问求根函数
```

#### 可能出现以下错误：

##### 1.~~unsupported operand type(s) for -: 'int' and 'str'~~ 不支持操作类型："int" 和 "str"

问题代码块：

```python
    a = input("输入变量a:")
    b = input("输入变量b:")
    c = input("输入变量c:")
```

原因：代码中需要用float、int类进行操作，没有数据类型转换会被录入为str类。导致没法参加公式计算。

解决方法：

```python
    a = float(input("输入变量a:"))
    b = float(input("输入变量b:"))
    c = float(input("输入变量c:"))
```

##### 2.~~missing 1 required positional argument: 'self'~~ 缺少一个位置参数self

问题代码块：

```python
class Equation:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
######################分割线#######################
Equation.getDiscriminant()
Equation.getRoot1()
Equation.getRoot1()
```

原因：Equation没有实例化，因为代码中Equation中定义了a,b,c三个基础变量。使用时需变量将类实例化

解决方法：

```python
Equation（a,b,c）.getDiscriminant()
Equation（a,b,c）.getRoot1()
Equation（a,b,c）.getRoot1()
```

##### 3.~~'Equation' object has no attribute 'delta'~~ Equation中没有属性"delta"

问题代码块：

```python
Equation（a,b,c）.getDiscriminant()
Equation（a,b,c）.getRoot1()
Equation（a,b,c）.getRoot1()
```

原因：实例化理解错误，翻看资料发现实例化的语句为  **对象名 = 类名（）** 即  **Eq = Equation(a,b,c)** 。

因此解决方法：

```python
Eq = Equation(a,b,c)
Eq.getDiscriminant()
Eq.getRoot()
```



#### 我认为要求根就直接一个Root函数比较方便，搞个Root1和Root2属实没必要，于是更改为了只有一个Root的版本：

```python
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
            return None
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
```

#### 代码完成，运行结果如下：

![image-20210427072412363](C:\Users\洪武\AppData\Roaming\Typora\typora-user-images\image-20210427072412363.png)

![image-20210427072431361](C:\Users\洪武\AppData\Roaming\Typora\typora-user-images\image-20210427072431361.png)