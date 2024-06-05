class Shap:
    def __init__(self, a):
        self.a = a

    def perimetr(self):
        pass


class Circle(Shap):

    def perimetr(self):
        pi = 3.14
        return (self.a * pi) * 2


class Rectangle(Shap):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def perimetr(self):
        return (self.a + self.b) * 2


class Triangle(Rectangle):
    def __init__(self, a, b, c):
        super(). __init__(a, b)
        self.c = c

    def perimetr(self):
        return self.a * self.b * self.c


circle1 = Circle(5)
rectangle1 = Rectangle(5, 7)
triangle1 = Triangle(4, 5, 6)
print(triangle1.perimetr())