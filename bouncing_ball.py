"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

#Global variable
ball = GOval(SIZE, SIZE)
window = GWindow(800, 500, title='bouncing_ball.py')
vy=0
s1 = False
c=0
def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball, x=START_X, y=START_Y)
    ball.filled = True
    onmouseclicked(drew)
    print('1')
def drew(mouse):
    global vy
    global c
    global s1
    print('2')
    if s1 == False:
        while True:
            s1=True
            if c >= 3:
                break
            ball.move(VX, vy)
            vy = vy + GRAVITY
            if ball.y + ball.height >= window.height:
                vy = -vy * REDUCE
            if ball.x >= window.width:
                c += 1
                window.add(ball, x=START_X, y=START_Y)
                ball.filled = True
                vy = 0
                s1= False
                break
            pause(DELAY)
























if __name__ == "__main__":
    main()
