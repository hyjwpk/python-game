import turtle
from Game import Game


class Go(Game):
    def __init__(self, type='mouse', simulations=1000) -> None:
        self._state = {'player': 0}
        self.players = [self.draw_black, self.draw_white]
        self.arr = [[0 for i in range(19)] for j in range(19)]
        turtle.setup(760, 760)
        turtle.title('Go')
        turtle.hideturtle()
        turtle.tracer(False)
        self.grid()
        super().__init__('go', self.show, type, simulations)
        if type == 'mouse':
            turtle.onscreenclick(self.tap)
        else:
            while not self.state.is_terminal():
                self.play_game()
        turtle.done()

    def grid(self):
        turtle.home()
        for i in range(19):  # 画横向
            turtle.up()
            turtle.goto(-360, -360+i*40)
            turtle.down()
            turtle.fd(720)
        turtle.left(90)
        for i in range(19):  # 画竖向
            turtle.up()
            turtle.goto(-360+i*40, -360)
            turtle.down()
            turtle.fd(720)

        turtle.up()  # 画标点
        turtle.goto(0, 0)
        turtle.dot()
        turtle.goto(240, 240)
        turtle.dot()
        turtle.goto(-240, 240)
        turtle.dot()
        turtle.goto(240, -240)
        turtle.dot()
        turtle.goto(-240, -240)
        turtle.dot()
        turtle.update()

    def draw_black(self, x, y):
        turtle.goto(x, y)
        turtle.dot(20)

    def draw_white(self, x, y):
        turtle.goto(x+10, y)
        turtle.down()
        turtle.circle(10)
        turtle.up()

    def floor(self, value):
        return int(((value + 360) / 40) + 0.5) * 40 - 360

    def draw(self, x, y):
        x = self.floor(x)
        y = self.floor(y)
        player = self._state['player']
        draw = self.players[player]
        draw(x, y)
        turtle.update()
        self._state['player'] = not player

    def show(self, str):
        self.arr = [[0 for i in range(19)] for j in range(19)]
        str = str.split('\n')[2:21]
        turtle.clear()
        self.grid()
        i = 0
        for substr in str:
            j = 0
            for ch in substr:
                if ch == '+':
                    j += 1
                elif ch == 'X':
                    self.arr[i][j] = 1
                    self._state['player'] = 0
                    self.draw(-360+j*40, 360-i*40)
                    j += 1
                elif(ch == 'O'):
                    self.arr[i][j] = 1
                    self._state['player'] = 1
                    self.draw(-360+j*40, 360-i*40)
                    j += 1
            i += 1

    def tap(self, x, y):
        x = int(((x + 360) / 40) + 0.5)
        y = int(((y + 360) / 40) + 0.5)
        position = str(x + y*19)
        if self.arr[18 - y][x] == 1:
            return
        for i in range(2):
            self.play_game(position)


if __name__ == "__main__":
    Go()
