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




