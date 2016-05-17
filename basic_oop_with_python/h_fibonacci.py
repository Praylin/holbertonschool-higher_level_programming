"""Function that computes the n numbers in fibonacci series"""
def fibonacci(x):
    a = 0
    b = 1
    c = 0
    if (x == 1):
        return 1
    else:
        for i in range (1, x):
            c = a + b
            a = b
            b = c
        return c
