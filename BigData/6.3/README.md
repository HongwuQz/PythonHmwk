### Python:定义一个汽车类，并在类中定义一个move方法

​	定义一个汽车类，并在类中定义一个move方法，然后分别创建BMW_X9、AUDI_A9对象，并添加颜色、马力、型号等属性，然后分别打印出属性值、调用move方法（使用__init__方法完成属性赋值）

#### 分析：

​	没啥好分析的，问题给的很明确了，直接开搞！

#### 代码如下：

```python
class Car:

    def __init__(self,color,model,horsepower):  #用init完成属性赋值
        self.color = color
        self.model = model
        self.horsepower = horsepower
    def move(self):     #move函数的实现
        print("一辆{}的{}飞驰而过，目测马力{}".format(self.color,self.model,self.horsepower))

if __name__ == '__main__':
    BMW_X9 = Car('绿色','BMW_X9','120码')
    AUDI_A9 = Car('红色','AUDI_A9','180码')
    BMW_X9.move()
    AUDI_A9.move()
```

输出结果：

![image-20210428144543526](C:\Users\洪武\AppData\Roaming\Typora\typora-user-images\image-20210428144543526.png)

