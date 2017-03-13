# rectangle has
#length -float/int
#width - float/int

#can-dos
#area - float/int
#perimeter - float/int
#size relative - string
#isSquare - boolean

class Rectangle:

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def getArea(self):
        area = self.length * self.width
        return area

    def getPerimeter(self):
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter

    def compareSz(self, other):
        areaself = self.getArea()
        areaother = other.getArea()
        if areaself > areaother:
            return True
        else:
            return False

    def isSquare(self):
        if self.length == self.width:
            return True
        else:
            return False

rec2 = Rectangle(5,10)


rec = Rectangle(33,8)
print(rec.getArea())
print(rec.getPerimeter())
print(rec.isSquare())

print(rec.compareSz(rec2))
