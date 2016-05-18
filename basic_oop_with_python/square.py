class Square:
    #constructor
    def __init__(self, side_length):
        self.__side_length = side_length
        self.name = "square"

    #destructor
    def __del__(self):
        pass

    #getter for color
    def get_color(self):
        return self.__color

    #setter for color
    def set_color(self, color):
        self.__color = color

    #setter for center
    def set_center(self, center):
        self.__center = [0, 0]

    #getter for center
    def get_center(self):
        return self.__center

    def area(self):
        return self.__side_length * self.__side_length
