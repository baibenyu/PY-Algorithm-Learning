class Rectangle:

    def setRect(self,length,width):
        self.length = length
        self.width = width

    def getRect(self):
        print("长:%s,宽:%s" % (self.length,self.width))

    def getArea(self):
        print("面积为:%s" % (self.length*self.width))

a = Rectangle()
a.setRect(24,32)
a.getRect()
a.getArea()