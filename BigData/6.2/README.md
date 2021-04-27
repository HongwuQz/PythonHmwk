### Python|给出三个点，判断三角形是钝角、锐角还是直角三角形

​	定义代表二维坐标系上某个点的Point类（包括x、y两个属性），为该类提供一个方法用于计算两个Point之间的距离，再提供一个方法用于判断三个Point组成的三角形是钝角、锐角还是直角三角形

#### 数学分析：

两点间距离公式：
$$
\sqrt{(x^2_{1}-x^2_{2})+(y^2_{1}-y^2_{2})}
$$
三角形的判定方法：{a,b,c}为三角形三边

① a + b <= c 或 a - b >= c 时，无法构成三角形；

② $a^2+b^2<c^2$ 时，构成锐角三角形 ；

③ $a^2+b^2=c^2$ 时，构成直角三角形 ；

④ $a^2+b^2>c^2$ 时，构成钝角三角形 ；

#### 代码分析：

利用两点间距离公式求出三条边，并通过三角形的判定方法进行判定并输出结果。

> 需要注意的是，三角形的定义是任意情况而非存在。所以需要对边进行处理才能保证适配性，不能直接带公式进行判断。

对三条边进行排序，得到下面非三角形情况：
①$边_{min}$ + $边_{mid}$ < $边_{max}$ 

②$边_{max}$ - $边_{min}$ > $边_{mid}$ 

#### 分析完毕，代码实现如下：

```python
class Points:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getDistance(self,other):    #两点之间距离公式
        return ((self.x - other.x) ** 2+(self.y - other.y) ** 2)**0.5
    def type_triangle(self,p2,p3):
        self_p2 = self.getDistance(p2)
        self_p3 = self.getDistance(p3)
        p2_p3 = p2.getDistance(p3)
        #对三条边进行排序，即可直接用三边定理排出非三角形情况
        if  self_p2 > self_p3:
            self_p2,self_p3 = self_p3,self_p2
        if  self_p3 > p2_p3:
            self_p3,p2_p3 = p2_p3,self_p3

        if  self_p2 + self_p3 <= p2_p3 or p2_p3 - self_p2 >=self_p3:
            return print("不是三角形")
        elif  self_p2 ** 2 + self_p3 ** 2 < p2_p3 ** 2:
            return print("锐角三角形")
        elif  self_p2 ** 2 + self_p3 ** 2 == p2_p3 ** 2:
            return print("直角三角形")
        elif  self_p2 ** 2 + self_p3 ** 2 > p2_p3 ** 2:
            return print("钝角三角形")
if __name__ == '__main__':
    pt1 = Points(2,3)
    pt2 = Points(4,5)
    pt3 = Points(0,0)
    dis12 = pt1.getDistance(pt2)
    dis13 = pt1.getDistance(pt3)
    dis23 = pt2.getDistance(pt3)
    print(dis12,dis13,dis23)
    pt1.type_triangle(pt2,pt3)
```

#### 运行结果：

#### ![6.2.1](https://github.com/HongwuQz/PythonHmwk/blob/main/Pictr/6.2.1.png)
