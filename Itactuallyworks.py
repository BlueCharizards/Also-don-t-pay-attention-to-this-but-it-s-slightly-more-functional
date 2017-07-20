#define a function that takes a number and returns the cube of that number.
#define another funcion that takes a number as an argument.
#if that number is divisible by 3, it calls the first function.
#otherwise, it returns False.

def cube(z):
    return z**3

def three(a):
    if (a)%3 == 0:
        return cube(a)
    else:
        return False
