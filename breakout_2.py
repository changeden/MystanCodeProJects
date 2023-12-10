"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_2 import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3 # Number of attempts

# ＃Global varible

# ball_radius=10
s1= False
graphics = BreakoutGraphics()
lives=NUM_LIVES
def main():
    onmouseclicked(handle_click_1)

def handle_click_1(event):
    global s1
    global lives
    vx = graphics.get_velocity_x()
    vy = graphics.get_velocity_y()

    if not s1:
        while True:
            s1=True
            if lives==0:
                break
            if graphics.window is graphics.paddle and graphics.ball:
                break
            graphics.ball.move( graphics.get_velocity_x(), graphics.get_velocity_y())
            graphics.remove_obj()
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                graphics.reverse_x()
            if graphics.ball.y <= 0 or graphics.ball.y >= graphics.window.height:
                graphics.reverse_y()
            # graphics.ball.move(graphics.get_velocity_x(), graphics.get_velocity_y())
            # if graphics.ball.y >= graphics.window.height:
            #     graphics.set_ball_position()
            #     break
            pause(FRAME_RATE)
            if graphics.ball.y>graphics.window.height:
                lives-=1
                if lives >0:
                    graphics.set_ball_position()
                else:
                    break

                s1 = False
                break





    # Add animation loop here!


if __name__ == '__main__':
    main()
