import math


class Tr:
    def __init__(self, side1, side2, side3, angle1):
        # , angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        # self.angle2 = angle2
        # self.angle3 = angle3
        self.perim = side1 + side2 + side3

    def sg(self):
        return math.sqrt(
            self.perim / (self.perim - self.side1) * self.perim / (self.perim - self.side2) * self.perim / (
                        self.perim - self.side3))

    def type(self):
        if self.side1 == 90 or self.side2 == 90 or self.side3 == 90:
            return 'Прямоугольный'
        if self.side1 + self.side2 + self.side3 == 180:
            return 'Равносторонний'
        elif self.side1 == self.side2 and self.side1 == self.side3 and self.side2 == self.side3:
            return 'Равнобедренный'
        else:
            return 'non'
