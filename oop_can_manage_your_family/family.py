class Person:

    #Class attributes
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    #constructor
    def __init__(self, ide, first_name, date_of_birth, genre, eyes_color):

        self.last_name = ""
        if (ide < 0) or (not isinstance(ide, int)):
            raise Exception("id is not an integer")
        self.__id = ide
        if (not isinstance(first_name, basestring)) or (not first_name):
            raise Exception("string is != string")
        self.__first_name = first_name
        if ((len(date_of_birth) is not 3) and (all(isinstance(x, int) for x in date_of_birth))) or ((date_of_birth[1] < 1) or (date_of_birth[1] > 31)) or ((date_of_birth[0] < 1) or (date_of_birth[0] > 12)):
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth = date_of_birth
        if (not isinstance(genre, basestring)) or (not genre in Person.GENRES):
            raise Exception("genre is not valid")
        self.__genre = genre
        if (not isinstance(eyes_color, basestring)) or (not eyes_color in Person.EYES_COLORS):
            raise Exception("eyes_color is not valid")
        self.__eyes_color = eyes_color
        
    #destructor
    def __del__(self):
        pass

    #getters
    def get_id(self):
        return self.__id

    def get_eyes_color(self):
        return self.__eyes_color

    def get_genre(self):
        return self.__genre

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.last_name
