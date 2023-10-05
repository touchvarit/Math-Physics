from turtle import *
n=5
def square(sidelength=n):
    for i in range(60):
         for i in range(4):
            forward(sidelength)
            right(90)
         sidelength = sidelength + 5
         right(5)
square()
