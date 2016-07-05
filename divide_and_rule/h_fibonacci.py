''' script to find the fibonacci number using threads'''
import threading

class FibonacciThread(threading.Thread):

    def __init__(self, number):
        threading.Thread.__init__(self)
        self.__number = number
        if not(isinstance( number, int )):
            raise Exception("number is not an integer")

    def run(self):
        a = 0
        b = 1
        c = 0
        if (self.__number == 1):
            return 1
        else:
            for i in range (1, self.__number):
                c = a + b
                a = b
                b = c
            print str(self.__number) + '=>' + str(c)
