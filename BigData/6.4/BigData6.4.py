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
