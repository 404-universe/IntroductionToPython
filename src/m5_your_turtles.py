"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Andy Sadler.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(16 + 2/3)

turtle1 = rg.SimpleTurtle('turtle')
turtle2 = rg.SimpleTurtle('turtle')

turtle1.pen_up()
turtle1.speed = 10
turtle1.backward(200)
turtle1.left(90)
turtle1.forward(200)
turtle1.right(90)
turtle1.pen_down()

turtle2.pen = rg.Pen("red", 1)

distance1 = 400
distance2 = 50

for i in range(20):
    for j in range(4):
        turtle1.forward(distance1)
        turtle1.right(90)

    turtle1.pen_up()
    turtle1.forward(2)
    turtle1.right(90)
    turtle1.forward(2)
    turtle1.left(90)
    turtle1.pen_down()

    turtle2.forward(distance2)
    turtle2.backward(distance2)
    turtle2.left(360 / 20)

    distance1 -= 4

window.close_on_mouse_click()