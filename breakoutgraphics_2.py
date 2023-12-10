"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.h=brick_height
        self.w=brick_width
        self.b=ball_radius
        self.brick_c = brick_cols
        self.brick_r = brick_rows
        self.brick_o = brick_offset
        self.brick_s = brick_spacing
        self.p_o = paddle_offset
        self.p_w = paddle_width
        self.p_h = paddle_height

        # Create a graphical window, with some extra space
        window_width = self.brick_c * (self.w + self.brick_s) - self.brick_s
        window_height = self.brick_o + 3 * (self.brick_r * (self.h + self.brick_s) - self.brick_s)
        self.window = GWindow(width=window_width, height=window_height, title="title")
        # Create a paddle
        self.paddle = GRect(self.p_w, self.p_h)
        self.paddle.color='black'
        self.paddle.filled = True

        self.window.add(self.paddle ,x=(self.window.width-self.paddle.width)/2 , y=(self.window.height-self.brick_o))

        # Center a filled ball in the graphical window
        self.ball=GOval(self.b*2, self.b*2)
        self.ball.filled=True
        self.remove_obj()
        self.window.add(self.ball, x=(self.window.width) / 2 - self.b, y=(self.window.height) / 2 - self.b)
        # self.set_ball_position()

        # Default initial velocity for the ball]
        # self.__dx=0
        # self.__dy=0
        self.__dx = random.randint(1,MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED   #不隨意改變
        self.set_ball_velocity()
        # self.get_velocity_x()
        # self.get_velocity_y()


        # Initialize our mouse listeners

        onmousemoved(self.handle_click)

        # Draw bricks
        self.brick = GRect(self.w,self.h)
        self.brick.filled = True
        self.brick.color = 'red'
        self.set_brick_position()

    def get_velocity_x(self):
        return self.__dx

    def get_velocity_y(self):
        return self.__dy

    def reverse_x(self):
        self.__dx = -self.__dx

    def reverse_y(self):
        self.__dy = -self.__dy
    #
    # def reset_ball(self):
    #     self.set_ball_position()
    #     while self.ball.y>self.window.height-self.p_o-self.p_h:
    #         self.set_ball_position()
    #     self.set_ball_velocity()
    #     self.window.add(self.ball)

    def set_ball_position(self):
        # Irene
        self.window.add(self.ball, x= (self.window.width) / 2 - self.b, y=(self.window.height) / 2 - self.b)

    def set_ball_velocity(self):
        # self.__dx = random.randint(1,MAX_X_SPEED)
        # self.__dy = INITIAL_Y_SPEED   #不隨意改變
        if random.random() > 0.5:
            self.__dx = -self.__dx
        if random.random() > 0.5:
            self.__dy = -self.__dy



    def handle_click(self,event):
        self.paddle.y = self.window.height - self.p_o
        self.paddle.x = event.x
        if self.paddle.x > self.window.width-self.p_w:
            self.paddle.x = self.window.width-self.p_w
        if self.paddle.x <= 0:
            self.paddle.x = 0

    def set_brick_position(self):
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.brick = GRect(self.w, self.h)
                self.window.add(self.brick, x=j*(BRICK_SPACING+BRICK_WIDTH), y=i*(BRICK_SPACING+BRICK_HEIGHT))
                if i <= 2:
                    self.brick.filled = True
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                if 1 < i < 4:
                    self.brick.filled = True
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange '
                if 3 < i < 6:
                    self.brick.filled = True
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow '
                if 5 < i < 8:
                    self.brick.filled = True
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green '
                if 7 < i < 10:
                    self.brick.filled = True
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'

    def remove_obj(self):
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x + 2 * self.b, self.ball.y)
        obj3 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.b)
        obj4 = self.window.get_object_at(self.ball.x + 2 * self.b, self.ball.y + 2 * self.b)
        # Irene
        if obj1 is not None or obj2 is not None or obj3 is not None or obj4 is not None:
            if obj1 is self.paddle or obj2 is self.paddle or obj3 is self.paddle or obj4 is self.paddle:
                self.__dy *= -1
            else:
                if obj1 is not None:
                    self.__dy *= -1
                    self.window.remove(obj1)
                elif obj2 is not None:
                    self.__dy = -self.__dy
                    self.window.remove(obj2)
                elif obj3 is not None:
                    self.__dy = -self.__dy
                    self.window.remove(obj3)
                elif obj4 is not None:
                    self.__dy = -self.__dy
                    self.window.remove(obj4)

            # if obj1 is not None and self.paddle:
            #     self.__dx = -self.__dx
            #     self.__dy = -self.__dy

            # self.__dx = -self.__dx
            # self.__dy = -self.__dy
        # if obj4 is self.paddle:
        #     self.__dy = -self.__dy

            # self.__dx = -self.__dx
            # self.__dy = -self.__dy



        # obj2=self.window.get_object_at(self.ball.x+2*self.b,self.ball.y)
        # if obj2 is not None and self.paddle:
        #     self.__dx = -self.__dx
        #     self.__dy = -self.__dy

            # self.__dx = -self.__dx
            # self.__dy = -self.__dy
        # if obj3 is self.paddle:
        #     self.__dy = -self.__dy


        # obj4=self.window.get_object_at(self.ball.x+2*self.b,self.ball.y+2*self.b)
        # if obj4 is not None and obj4 is self.paddle:
        #     self.__dx = -self.__dx
        #     self.__dy = -self.__dy


            # self.__dx = -self.__dx
            # self.__dy = -self.__dy
        # if obj2 is self.paddle:
        #     self.__dy = -self.__dy


        # obj3=self.window.get_object_at(self.ball.x,self.ball.y+2*self.b)
        # if obj3 is not None and self.paddle:
        #     self.__dx = -self.__dx
        #     self.__dy = -self.__dy


    def reverse_x(self):
        self.__dx = -self.__dx

    def reverse_y(self):
        self.__dy = -self.__dy





