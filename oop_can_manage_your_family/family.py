import json
import os.path

def save_to_file(list, filename):
    with open(filename, 'w') as outfile:
        json.dump(list, outfile)
#
def load_from_file(filename):
    # data = []
    a = Person(2, "gfdhf", [07, 23, 1985], "Male", "Blue")
    if (isinstance(filename, basestring) and os.path.isfile(filename)):
        with open(filename, 'r') as data_file:
            data = json.load(data_file)
        for i in data:
            j = a.load_from_json(i)
            a.json ()
    else:
        raise Exception("filename is not valid or doesn't exist")


class Person:

    #Class attributes
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    #constructor
    def __init__(self, ide, first_name, date_of_birth, genre, eyes_color):

        self.last_name = ""
        self.is_married_to = 0
        if (ide < 0) or (not isinstance(ide, int)):
            raise Exception("id is not an integer")
        self.__id = id
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

    #Method which returns first name and last name
    def __str__(self):
        return "%s %s" %(self.__first_name, self.last_name)

    #Method which checks whether genre is Male
    def is_male(self):
        if self.__genre is "Male":
            return True
        else:
            return False

    #Method to find the age
    #Age has to be computed with the fix date: 05/20/2016
    def age(self):
        return 2016 - self.__date_of_birth[2] - ((05, 20) < (self.__date_of_birth[1], self.__date_of_birth[0]))

    #Function returns a hash
    def json(self):
        return {'id' : self.__id, 'genre' : self.__genre, 'eyes_color' : self.__eyes_color, 'date_of_birth' : self.__date_of_birth, 'first_name' : self.__first_name, 'last_name' : self.last_name}

    #Function sets values for all keys if the argument is a hash, otherwise raise an exception
    def load_from_json(self, json):
        if isinstance(json, dict):
            self.__id = json['id']
            self.__genre = json['genre']
            self.__eyes_color = json['eyes_color']
            self.__date_of_birth = json['date_of_birth']
            self.__first_name = json['first_name']
            self.last_name = json['last_name']
        else:
            raise Exception("json is not valid")

class Baby(Person):

    def need_help(self):
        return True

    def is_young(self):
        return True

    def can_run(self):
        return False

    def can_vote(self):
        return False

    def can_be_married(self):
        return False


class Teenager(Person):

    def can_run(self):
        return True

    def is_young(self):
        return True

    def need_help(self):
        return False

    def can_vote(self):
        return False

    def can_be_married(self):
        return False

class Adult(Person):

    def can_run(self):
        return True

    def can_vote(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_be_married(self):
        return True

class Senior(Person):

    def need_help(self):
        return True

    def can_vote(self):
        return True

    def is_young(self):
        return False

    def can_run(self):
        return False

    def can_be_married(self):
        return True
