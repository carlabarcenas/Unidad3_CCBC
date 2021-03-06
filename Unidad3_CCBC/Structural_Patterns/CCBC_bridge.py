#Autor: Carla del Carmen Barcenas Castillo
#Grupo: GITI9072-e
#Structural_Patterns

class DrawingAPIOne(object):
    """Implementation-specific abstraction:concrete class one"""
    def draw_circule(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

class DrawingAPITwo(object):
        """Implementation-specific abstraction: concrete class two"""
        def draw_circle(self, x, y, radius):
            print("API 2 drawing a circle at ({}, +")


class Circle(object):
    """implementation-independet abstraction: for example, there could be a retangle class!"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abtraction take care"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementation-independent"""
        self._radius *=percent

#Build the first circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
#Draw a circle
circle1.draw()

#Build the second Circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
#Draw a circle
circle2.draw()

