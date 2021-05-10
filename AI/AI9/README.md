### Python:用sklearn中的DecisionTreeClassifier，根据iris数据生成决策树



#### 需求包分析：

关键词：sklearn、DecisionTreeClassifier、iris数据、决策树

对应包：sklearn.tree.DecisionTreeClassifier、sklearn.datasets.load_iris、matplotlib.pyplot



##### 分析完毕，实现代码如下

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
iris_tree = tree.DecisionTreeClassifier(criterion='entropy')
iris_tree = iris_tree.fit(iris.data,iris.target)
plt.figure(1)
tree.plot_tree(iris_tree)
plt.show()
```

实验结果：

![image-20210509225655796](C:\Users\洪武\AppData\Roaming\Typora\typora-user-images\AI9.1.1.png)

#### 思考

我们是否可以用上面的方法对其他数据集进行分析？ 

我们先将iris的文件导出，看看里面的格式

```python
from sklearn.datasets import load_iris

with open("irisData.txt","w") as f:
    f.write(str(load_iris()))
```

得到结果：文件中为‘data’和'target'的两个数组

```
{'data': array([[5.1, 3.5, 1.4, 0.2],
       [4.9, 3. , 1.4, 0.2],
       [4.7, 3.2, 1.3, 0.2],
       [4.6, 3.1, 1.5, 0.2],
       [5. , 3.6, 1.4, 0.2],
       [5.4, 3.9, 1.7, 0.4],
       [4.6, 3.4, 1.4, 0.3]), 'target': array([0, 0, 0, 0, 0, 0, 0])
已删除多余部分，只保留说明性的前7个鸢尾花（iris）数据
```

所以要将西瓜树中所给的数据同样转变为‘data’和‘target’两个数组

##### 分析完毕，代码如下：

将西瓜数据集转化为相应形式：

```python
with open('walterMelonData.txt','r') as f:
    data = []
    for line in f.readlines():
        line = line.strip('\n') #用换行符作为行的识别符
        data.append(line.split(' ')) #行内数据用空格作为数据分割符
    data = np.array(data,dtype=float)
    watermelon_data = np.array(data[:,:8])
    watermelon_target = np.array(data[:,8])
print('数据集：',watermelon_data,'\n标签：',watermelon_target)
```

输出结果为：

![image-20210510082136062](C:\Users\洪武\AppData\Roaming\Typora\typora-user-images\AI9.1.png)

得到结果以后，我们就可以直接带入到之前的那个代码中。即：

```python
import matplotlib.pyplot as plt
from sklearn import tree
import numpy as np

with open('walterMelonData.txt','r') as f:
    data = []
    for line in f.readlines():
        line = line.strip('\n')
        data.append(line.split(' '))
    data = np.array(data,dtype=float)
    watermelon_data = np.array(data[:,:8])
    watermelon_target = np.array(data[:,8])

watermelon_tree = tree.DecisionTreeClassifier(criterion='entropy')
watermelon_tree = watermelon_tree.fit(watermelon_data,watermelon_target)
plt.figure(1)
tree.plot_tree(watermelon_tree)
plt.show()
```

输出结果：

![image-20210510082305069](C:\Users\洪武\AppData\Roaming\Typora\typora-user-images\AI9.2.1.png)

#### 遇到的问题

##### [二维数组切割的格式](https://blog.csdn.net/Alphy_Hongwu/article/details/116585616)