import turtle
from Game import Game


class Hex(Game):
    def __init__(self, type='mouse', simulations=1000) -> None:
        self._state = {'player': 0}
        self.players = [self.draw_black, self.draw_white]
        self.arr = [[0 for i in range(11)] for j in range(11)]
        turtle.setup(600, 400)
        turtle.title('Hex')
        turtle.hideturtle()
        turtle.tracer(False)
        self.grid()
        super().__init__('hex', self.show, type, simulations)
        if type == 'mouse':
            turtle.onscreenclick(self.tap)
        else:
            while not self.state.is_terminal():
                self.play_game()
        turtle.done()

    def hexagon(self, x, y):
        turtle.penup()
        turtle.goto(x, y-20)
        turtle.pendown()
        turtle.circle(20, steps=6)

    def grid(self):
        for i in range(11):
            for j in range(11):
                self.hexagon(-250+20/2*(3**0.5)*(2*j+i), 150-30*i)
        turtle.update()

    def draw_black(self, x, y):
        turtle.fillcolor('red')
        turtle.begin_fill()
        self.hexagon(x, y)
        turtle.end_fill()
        turtle.update()

    def draw_white(self, x, y):
        turtle.fillcolor('blue')
        turtle.begin_fill()
        self.hexagon(x, y)
        turtle.end_fill()
        turtle.update()

    def draw(self, x, y):
        player = self._state['player']
        draw = self.players[player]
        draw(x, y)
        self._state['player'] = not player

    def show(self, str):
        self.arr = [[0 for i in range(11)] for j in range(11)]
        str = str.split('\n')
        turtle.clear()
        self.grid()
        i = 0
        for substr in str:
            j = 0
            for ch in substr:
                if ch == '.':
                    j += 1
                elif ch == 'x' or ch == 'y' or ch == 'z' or ch == 'X':
                    self.arr[i][j] = 1
                    self._state['player'] = 0
                    self.draw(-250+20/2*(3**0.5)*(2*j+i), 150-30*i)
                    j += 1
                elif ch == 'o' or ch == 'p' or ch == 'q' or ch == 'O':
                    self.arr[i][j] = 1
                    self._state['player'] = 1
                    self.draw(-250+20/2*(3**0.5)*(2*j+i), 150-30*i)
                    j += 1
            i += 1

    def tap(self, x, y):
        for i in range(11):
            for j in range(11):
                X = -250+20/2*(3**0.5)*(2*j+i)
                Y = 150-30*i
                if x >= X - 20 and x <= X + 20 and y >= Y - 20 and y <= Y + 20:
                    if x >= X - 20 and x <= X:
                        if y > Y - 10 - 10 * (x - (X-20))/(10*(3**0.5)) and y < Y + 10 + 10 * (x - (X-20))/(10*(3**0.5)):
                            if self.arr[i][j] == 1:
                                return
                            position = str(i*11+j)
                            for i in range(2):
                                self.play_game(position)
                            return
                    elif x >= X and x <= X + 20:
                        if y > Y - 10 - 10 * ((X+20) - x)/(10*(3**0.5)) and y < Y + 10 + 10 * ((X+20) - x)/(10*(3**0.5)):
                            if self.arr[i][j] == 1:
                                return
                            position = str(i*11+j)
                            for i in range(2):
                                self.play_game(position)
                            return


if __name__ == "__main__":
    Hex()
