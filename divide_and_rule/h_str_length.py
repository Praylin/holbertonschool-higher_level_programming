'''script finds the length of string'''
import threading

class StrLengthThread(threading.Thread):
    def __init__(self, word):
        threading.Thread.__init__(self)
        self.__word = word
        if not(isinstance( word, basestring )):
            raise Exception("word is not a string")

    def run(self):
        StrLengthThread.total_str_length = StrLengthThread.total_str_length + len(self.__word)
