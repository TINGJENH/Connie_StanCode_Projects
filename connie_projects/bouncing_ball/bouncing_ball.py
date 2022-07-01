"""
File: bouncing_ball.py
Name: Connie Huang
-------------------------
1. set num_trial (how many click occurred) and mouse_clicked (whether click has occurred) as global variables.
2. Add a dot to (START_X, START_Y).
3. After clicking, 4 things will occur:
   3-1. remove the original dot
   3-2. add 1 to num_trial
   3-3. ball start bouncing.
   3-4. mouse_clicked will be 1 at first and becomes 0 after finish the bouncing.
        (when mouse_clicked equals to 1, nothing will happen after clicking)
4. When the ball has left the width of the window, it will go back to (START_X, START_Y)
5. When num_trial == 3, nothing will happen after clicking
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

window = GWindow(800, 500, title='bouncing_ball.py')
num_trial = 0
# Used to track mouse status
mouse_clicked = 0
start_dot = GOval(SIZE, SIZE, x=START_X - SIZE / 2, y=START_Y - SIZE / 2)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(start_bouncing)
    start_dot.filled = True
    start_dot.fill_color = 'black'
    window.add(start_dot)


def start_bouncing(mouse):
    global num_trial, mouse_clicked
    if num_trial < 3 and mouse_clicked == 0:
        y_velocity = 0
        while True:
            mouse_clicked = 1
            y_velocity += GRAVITY
            start_dot.move(VX, y_velocity)
            if start_dot.y + SIZE / 2 >= window.height:
                y_velocity = - y_velocity * REDUCE

            if start_dot.x >= window.width:
                num_trial += 1
                start_dot.x = START_X - SIZE / 2
                start_dot.y = START_Y - SIZE / 2
                break
            pause(DELAY)
        mouse_clicked = 0


if __name__ == "__main__":
    main()
