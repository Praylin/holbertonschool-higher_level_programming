'''Reverse string using threading'''
import threading

class ReverseStrThread(threading.Thread):
    def __init__(self, word):
        threading.Thread.__init__(self)
        self.__word = word
        if not(isinstance( word, basestring )):
            raise Exception("word is not a string")

    def run(self):
        ReverseStrThread.sentence = ReverseStrThread.sentence + " " + self.__word[::-1]
