import turtle
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from Game import Game


class Tictactoe(Game):
    def __init__(self, type='mouse', simulations=1000) -> None:
        self._state = {'player': 0}
        self.players = [self.drawx, self.drawo]
        self.arr = [[0 for i in range(3)] for j in range(3)]
        turtle.setup(420, 420)
        turtle.title('Tictactoe')
        turtle.hideturtle()
        turtle.tracer(False)
        self.grid()
        super().__init__('tic_tac_toe', self.show, type, simulations)
        if type == 'mouse':
            turtle.onscreenclick(self.tap)
        else:
            while not self.state.is_terminal():
                self.play_game()
        turtle.done()

    def line(self, a, b, x, y):
        turtle.up()
        turtle.goto(a, b)
        turtle.down()
        turtle.goto(x, y)

    def grid(self):
        self.line(-67, 200, -67, -200)
        self.line(67, 200, 67, -200)
        self.line(-200, -67, 200, -67)
        self.line(-200, 67, 200, 67)
        turtle.update()

    def drawx(self, x, y):
        self.line(x, y, x + 133, y + 133)
        self.line(x, y + 133, x + 133, y)
        turtle.update()

    def drawo(self, x, y):
        turtle.up()
        turtle.goto(x + 67, y + 5)
        turtle.down()
        turtle.circle(62)
        turtle.update()

    def floor(self, value):
        return ((value + 200) // 133) * 133 - 200

    def draw(self, x, y):
        """Draw X or O in tapped square."""
        x = self.floor(x)
        y = self.floor(y)
        player = self._state['player']
        draw = self.players[player]
        draw(x, y)
        turtle.update()
        self._state['player'] = not player

    def show(self, str):
        self.arr = [[0 for i in range(3)] for j in range(3)]
        str = str[:]
        turtle.clear()
        self.grid()
        for i in range(3):
            for j in range(3):
                if(str[i*4+j] != '.'):
                    self.arr[i][j] = 1
                    self._state['player'] = 0 if str[i*4+j] == 'x' else 1
                    self.draw(-133+j*133, 133-i*133)

    def tap(self, x, y):
        x = int((x + 200) // 133)
        y = int(2 - (y + 200) // 133)
        position = str(x + y*3)
        if self.arr[y][x] == 1:
            return
        for i in range(2):
            self.play_game(position)


if __name__ == "__main__":
    Tictactoe()
