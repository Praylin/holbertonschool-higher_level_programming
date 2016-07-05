'''Finds the length of the string given as command line argument using threads'''
import threading
import sys

class StrLenThread(threading.Thread):
        def __init__(self, word):
            threading.Thread.__init__(self)
            self.__word = word
            if not(isinstance( word, basestring )):
                raise Exception("word is not a string")

        def run(self):
            StrLenThread.total_str_length = StrLenThread.total_str_length + len(word)

str_length_threads = []
words = sys.argv[1].split(" ")
StrLenThread.total_str_length = len(words) - 1
for word in words:
    str_length_thread = StrLenThread(word)
    str_length_threads += [str_length_thread]
    str_length_thread.start()

for t in str_length_threads:
    t.join()

print "%d" % StrLenThread.total_str_length
