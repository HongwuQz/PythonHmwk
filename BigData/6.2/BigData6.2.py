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