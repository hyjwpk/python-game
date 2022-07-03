import turtle
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from Game import Game


class Y(Game):
    def __init__(self, type='mouse', simulations=1000) -> None:
        self._state = {'player': 0}
        self.players = [self.draw_black, self.draw_white]
        self.arr = [[0 for i in range(19)] for j in range(19)]
        turtle.setup(700, 700)
        turtle.title('Y')
        turtle.hideturtle()
        turtle.tracer(False)
        self.grid()
        super().__init__('y', self.show, type, simulations)
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
        for i in range(20):
            for j in range(i):
                self.hexagon(350+20/2*(3**0.5)*(j-2*i), 230-30*j)
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
        self.arr = [[0 for i in range(19)] for j in range(19)]
        str = str.split('\n')[1:20]
        turtle.clear()
        self.grid()
        i = 0
        for substr in str:
            j = 0
            for ch in substr:
                if ch == '.':
                    j += 1
                elif ch == 'O':
                    self.arr[i][j] = 1
                    self._state['player'] = 0
                    self.draw(350+20/2*(3**0.5)*(i-2*(19-j)), 230-30*i)
                    j += 1
                elif ch == '@':
                    self.arr[i][j] = 1
                    self._state['player'] = 1
                    self.draw(350+20/2*(3**0.5)*(i-2*(19-j)), 230-30*i)
                    j += 1
            i += 1

    def tap(self, x, y):
        for i in range(20):
            for j in range(i):
                X = 350+20/2*(3**0.5)*(j-2*i)
                Y = 230-30*j
                if x >= X - 20 and x <= X + 20 and y >= Y - 20 and y <= Y + 20:
                    if x >= X - 20 and x <= X:
                        if y > Y - 10 - 10 * (x - (X-20))/(10*(3**0.5)) and y < Y + 10 + 10 * (x - (X-20))/(10*(3**0.5)):
                            if self.arr[j][19-i] == 1:
                                return
                            position = str(19*j+19-i)
                            for i in range(2):
                                self.play_game(position)
                            return
                    elif x >= X and x <= X + 20:
                        if y > Y - 10 - 10 * ((X+20) - x)/(10*(3**0.5)) and y < Y + 10 + 10 * ((X+20) - x)/(10*(3**0.5)):
                            if self.arr[j][19-i] == 1:
                                return
                            position = str(19*j+19-i)
                            for i in range(2):
                                self.play_game(position)
                            return


if __name__ == "__main__":
    Y()
