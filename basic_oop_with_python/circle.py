"""Find the area of a circle"""

import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        #self.__center = [0, 0]
        #self.__color = "red"
        self.name = "circle"

    def __del__(self):
        pass

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def set_center(self, center):
        self.__center = [0, 0]

    def area(self):
        radius = math.pi * self.__radius * self.__radius
        return radius
