### Python:类与对象训练题

完成下列小题

1）创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息

2）创建Student类，继承Person类，属性有学院college

，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，

创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。

重写__str__方法，返回student的信息。

3）创建Teacher类，继承Person类，属性有学院college，专业professional

，重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。

创建teachObj方法，返回信息为‘今天讲了如何用面向对象设计程序’

4）创建三个学生对象，分别打印其详细信息

5）创建一个老师对象，打印其详细信息

6）学生对象调用learn方法

7）将三个学员添加至列表中，通过循环将列表中的对象打印出来，print(Student对象)。

#### 代码实现：

```python
class Person:
    def __init__(self, name, age, sex):
        self.age = age
        self.name = name
        self.sex = sex

    def personInfo(self):
        print("{},{},{}".format(self.name, self.sex, self.age))


class Teacher(Person):
    def __init__(self, name, sex, age, college, professional):
        super(Teacher, self).__init__(name, sex, age)
        self.college = college
        self.professional = professional

    def personInfo(self):
        Person.personInfo(self)
        print("教于{}{}".format(self.college, self.professional))

    def teachObj(self):
        self.Obj = '面向对象设计程序'
        print("今天讲了如何用{}".format(self.Obj))
        return self.Obj


class Student(Person):
    def __init__(self, name, sex, age, college, clas, ):
        super().__init__(name, sex, age)
        self.college = college
        self.clas = clas

    def personInfo(self):
        Person.personInfo(self)
        return "就读于{}{}".format(self.college, self.clas)

    def learn(self):
        self.teachObj = Teacher.teachObj(self)
        print("老师,{}我终于学会了！".format(self.teachObj))


if __name__ == '__main__':
    stu1 = Student("张三", "男", "21岁", "财经政法大学", "非法学院")
    stu2 = Student("李四", "女", "21岁", "电子科技大学", "电子信息学院")
    stu3 = Student("王五", "男", "21岁", "华东电子科技大学", "电子信息学院")
    tea1 = Teacher("赵六", "男", "24岁", "财经政法大学", "非法学院")
    tea1.personInfo()
    stu1.learn()
    stuList = [stu1, stu2, stu3]
    for stu in stuList:
        print(stu.personInfo())
```



#### 遇到的问题:

##### ~~TypeError: descriptor '__init__' requires a 'super' object but received a 'str'~~ init需要的是super对象，不是str字符串

```python
    def __init__(self,name,sex,age,college,clas,):
        super.__init__(name,sex,age)
        self.college = college
        self.clas = clas
```

##### 分析原因:super（）才是对象的形式，如果少了括号就变成了“super”这个str字符串调用__init__，所以会出现这种报错。

##### 解决：super后面价格括号，super字符就变成super对象了

```python
    def __init__(self,name,sex,age,college,clas,):
        super().__init__(name,sex,age)
        self.college = college
        self.clas = clas
```

