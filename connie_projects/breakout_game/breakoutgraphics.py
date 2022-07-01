"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
1. Set the environment of the window, incl. bricks, paddle, ball, etc.
2. Set up required methods.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.num_trial = 0
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle_x = (self.window.width - paddle_width)/2
        self.paddle_y = self.window.height - paddle_offset
        self.paddle = GRect(paddle_width, paddle_height, x=self.paddle_x, y=self.paddle_y)
        self.paddle_offset = paddle_offset
        self.paddle_height = PADDLE_HEIGHT
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball_start_x = (self.window.width-ball_radius)/2
        self.ball_start_y = (self.window.height-ball_radius)/2
        self.ball = GOval(ball_radius*2, ball_radius*2, x=self.ball_start_x, y=self.ball_start_y)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.mouse_clicked = False
        onmouseclicked(self.ball_position)
        onmousemoved(self.paddle_position)

        # Draw bricks
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        self.brick_spacing = brick_spacing
        self.num_brick = self.brick_rows * self.brick_cols
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.color = 'black'
                self.window.add(self.brick, x=0+(self.brick.width+brick_spacing)*i, y=brick_offset+(self.brick.height+brick_spacing)*j)
                if j % 2 == 1:
                    self.brick.color = 'rosybrown'
                    self.brick.filled = True
                    self.brick.fill_color = 'rosybrown'
                else:
                    self.brick.color = 'lavenderblush'
                    self.brick.filled = True
                    self.brick.fill_color = 'peachpuff'

    # To differentiate whether object is a paddle.
    def is_paddle(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) is self.paddle:
            is_paddle = True
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y) is self.paddle:
            is_paddle = True
        elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height) is self.paddle:
            is_paddle = True
        elif self.window.get_object_at(self.ball.x + self.ball.height, self.ball.y + self.ball.height) is self.paddle:
            is_paddle = True
        else:
            is_paddle = False
        return is_paddle

    # If object is bricks, will remove them. If object is paddle, ball __dy will time -1.
    def remove_bricks_or_rebound(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None and self.window.get_object_at(self.ball.x, self.ball.y) is not self.paddle:
            brick = self.window.get_object_at(self.ball.x, self.ball.y)
            self.window.remove(brick)
            self.__dy = - self.__dy
            self.num_brick -= 1
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y) is not None and self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y) is not self.paddle:
            brick = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
            self.window.remove(brick)
            self.__dy = - self.__dy
            self.num_brick -= 1
        elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height) is not None and self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height) is not self.paddle:
            brick = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
            self.window.remove(brick)
            self.__dy = - self.__dy
            self.num_brick -= 1
        elif self.window.get_object_at(self.ball.x + self.ball.height, self.ball.y + self.ball.height) is not None and self.window.get_object_at(self.ball.x + self.ball.height, self.ball.y + self.ball.height) is not self.paddle:
            brick = self.window.get_object_at(self.ball.x + self.ball.height, self.ball.y + self.ball.height)
            self.window.remove(brick)
            self.__dy = - self.__dy
            self.num_brick -= 1
        else:
            pass
        if self.is_paddle() is True:
            # after the direction has been changed, we don't need to change direction again.
            if self.__dy > 0:
                self.__dy = - self.__dy
        return self.num_brick

    def ball_position(self, mouse):
        """
        :param mouse: mouse click detect mouse event
        :return:
        """
        # add if to only change the velocity when the ball is not moving.
        if self.__dy == 0 and self.__dx == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
            if random.random() > 0.5:
                self.__dy = - self.__dy
            self.mouse_clicked = True

    # Change velocity when ball reaches the boundaries
    def in_the_zone(self):
        if self.ball.x + self.ball.width >= self.window.width or self.ball.x <= 0:
            self.__dx = - self.__dx
        if self.ball.y <= 0:
            self.__dy = - self.__dy

    # Make sure ball will go back to the starting point.
    def reset_ball(self):
        if self.ball.y+self.ball.width >= self.window.height:
            self.ball.y = self.ball_start_y
            self.ball.x = self.ball_start_x
            self.__dx = 0
            self.__dy = 0

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def paddle_position(self, mouse):
        self.paddle_x = mouse.x - self.paddle.width/2
        if self.paddle_x + self.paddle.width > self.window.width:
            self.paddle_x = self.window.width - self.paddle.width
        if self.paddle_x < self.paddle.width/2:
            self.paddle_x = 0
        # remember to assign paddle_x to paddle.x
        self.paddle.x = self.paddle_x
