"""Find the area of a circle"""

import math

class Circle:
    #constructor
    def __init__(self, radius):
        self.__radius = radius
        self.name = "circle"

    #destructor
    def __del__(self):
        pass

    #getter for color
    def get_color(self):
        return self.__color

    #setter for color
    def set_color(self, color):
        self.__color = color

    #getter for radius
    def get_radius(self):
        return self.__radius

    #setter for radius
    def set_radius(self, radius):
        self.__radius = radius

    #setter for center
    def set_center(self, center):
        self.__center = [0, 0]

    #getter for center
    def get_center(self):
        return self.__center

    #finds and return area
    def area(self):
        return math.pi * self.__radius * self.__radius
