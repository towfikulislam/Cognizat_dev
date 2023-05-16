'''Impporting module form python library to use. Module is a file with bunch of codes'''

'''right side of = sign creating code object in computer memory. the left side of = sign a assigned name. 
turtle is the main module and .Turtle is the block of codes written in main turtle module.'''

'''Here block of codes is used from main module turtle like look for forward block or right block. These
are called method. The parethesis () are for input like what those method needs to do'''
# following all these are called assignments. There are different categories.
# 1. simple statements
# import statement
import turtle
#assignment statement
iqra = turtle.Turtle() #statements
name_dif = ["Faria"]
# call statement
iqra.forward(100)
iqra.right(90)

# 2. compound statement
for name in name_dif :
    iqra.forward(50)
    iqra.right(90)

# range replaces like how many times you need to run something in your loop. Instead of saying x= [1,2,3,4] 
# we can do following:

for looping in range(4):
    iqra.forward(30)
    iqra.right(60)

# When we define a function, we specify its parameters:
def spiral(sides, turn, color, width):

# When we call a function, we specify its arguments:
spiral(150, -30, "blue", 10)


# An expression is a piece of code that resolves to some value. Within an expression, there are operators and operands.
# Operators: indicate what operation is to be performed (such as addition or subtraction). Ex: +, -, *, /
# Operands: are the numbers (or other values) on which we want to perform the operations.Ex: can be any
# numbers like 2, 8

iqra.forward(100 / 2)

# to drea a angle we can divide 360 by the corners of shape we are trying to draw. like if you want to draw
# octagon just simply divide 360 by 8 because octagon has 8 corners. This will give you the angle we need to 
# put in the code to make octagon.

angle = 360/8 #(number of corners/sides, in this case 8 for octagon)

# Function: function is used to use same writtern block of codes again again just by "call funtion option".
# a function will not run unless you call it>

def draw_square(length):  # this is how to define a function.
    jack = turtle.Turtle()
    jack.color("yellow")
    for sides in range(4):
        jack.forward(length)
        jack.right(90)
draw_square(40) # this used to call function to make code run
draw_square(30)
draw_square(20)

# conditional/if/else statement: Basically we write code in the following manner to give our conditions
# in the code. Like if side is equal to 4 then color is purple otherwise yellow. Lets look at this through code below:
import turtle
bob = turtle.Turtle()
bob.color("yellow")
for sides in [1,2,4]:
    if side == 4:
        bob.color("purple")

for side in range(4):
    if side == 1:
        jack.color("blue")
    else:
        jack.color("yellow")
    jack.forward(100)
    jack.right(90)

# Math/division: How would we actually use this in some code? Here's one way: Modulo is really common in a particular pattern 
# with for and if. Here's an example:

for n in range(12):
   if n % 3 == 0:
      draw_triangle()
   else:
      draw_square()

# This loop will run 12 times. When n is 0, 3, 6, or 9, the result will be 0. And that means the draw_triangle 
# function will be called. When n is 1, 2, 4, 5, 7, 8, 10, or 11, the draw_square function will be called.
