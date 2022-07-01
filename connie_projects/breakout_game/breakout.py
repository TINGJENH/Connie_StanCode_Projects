"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE: 
1. When I still have life and I haven't clicked, we can get the ball moving in the boundaries.
   If it touches bricks, bricks will be removed. If it touches paddle, it will rebound.
2. When ball_y is higher than y, we will lose one life.
3. When life becomes zero or all bricks are cleared, the game will end.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    lives_left = NUM_LIVES
    graphics = BreakoutGraphics()
    print(graphics.mouse_clicked)
    while True:
        if lives_left > 0 and graphics.mouse_clicked is False:
            graphics.mouse_clicked = True
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.in_the_zone()
            graphics.remove_bricks_or_rebound()
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.reset_ball()
            lives_left -= 1
        if lives_left <= 0 or graphics.num_brick == 0:
            break
        graphics.mouse_clicked = False
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
