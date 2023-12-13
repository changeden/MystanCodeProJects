"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow
DELAY =100
# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	order = ORDER-1
	line = GLine(UPPER_LEFT_X,UPPER_LEFT_Y, UPPER_LEFT_X+LENGTH, UPPER_LEFT_Y)
	window.add(line)
	line = GLine(UPPER_LEFT_X, UPPER_LEFT_Y, UPPER_LEFT_X + LENGTH/2, UPPER_LEFT_Y+LENGTH*0.866)
	window.add(line)
	line = GLine(UPPER_LEFT_X + LENGTH/2, UPPER_LEFT_Y+LENGTH*0.866, UPPER_LEFT_X+LENGTH, UPPER_LEFT_Y)
	window.add(line)
	sierpinski_triangle(order, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order,length, upper_left_x, upper_left_y):
	"""
	:param order:
	:param length:
	:param upper_left_x:
	:param upper_left_y:
	# :return:
	"""
	if order == 0:
		pass
	else:
		line = GLine(length*0.5+upper_left_x,upper_left_y, 0.5*0.5*length+upper_left_x,0.5*length*0.866+upper_left_y)
		window.add(line)
		line = GLine(0.5*0.5*length+upper_left_x, 0.5*length*0.866+upper_left_y, 3/4*length+upper_left_x,0.866*length/2+ upper_left_y)
		window.add(line)
		line = GLine(3/4*length+upper_left_x,0.866*length/2+upper_left_y, length*0.5+upper_left_x,upper_left_y)
		window.add(line)

		pause(DELAY) #緩慢show 出來, 用pause
		#upper left
		sierpinski_triangle(order - 1, length / 2,upper_left_x, upper_left_y)
		#upper right
		sierpinski_triangle(order-1, length / 2, length*0.5+upper_left_x,upper_left_y)
		#mid down point
		sierpinski_triangle(order-1, length / 2, 0.5*0.5*length+upper_left_x,0.5*length*0.866+upper_left_y)





if __name__ == '__main__':
	main()