"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE=10

window = GWindow()
count=0   #global variable
last_x =0
last_y =0
new_x=0
new_y=0
hole = GOval(SIZE, SIZE)
def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)
    print('1')

def draw_line(mouse):
    """
    :param mouse: draw line step1.first add oval hole. step2.Second add line and remove first oval.
    """
    global count
    global last_x
    global last_y
    global new_x
    global new_y
    count+=1
    print('2')
    if count % 2 !=0:
        # hole = GOval(SIZE, SIZE)
        last_x = mouse.x
        last_y = mouse.y
        window.add(hole, x=last_x, y=last_y)
        print('3')
    if count % 2 == 0:
        new_x = mouse.x
        new_y = mouse.y
        line = GLine(last_x,last_y, new_x, new_y)
        window.add(line)
        window.remove(hole)     #move the ori.oval
        print('4')




if __name__ == "__main__":
    main()
