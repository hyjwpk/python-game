import argparse
from openspiel.game.Tictactoe import Tictactoe
from openspiel.game.Go import Go
from openspiel.game.Y import Y
from openspiel.game.Hex import Hex
from openspiel.game.Havannah import Havannah
import freegames_extern.snake
import freegames_extern.paint
import os

path = os.path.abspath('.') + '/freegames'

freegameslist = [
    'Ant',
    'Bagles',
    'Boom',
    'Bounce',
    'Cannon',
    'Connect',
    'Crypto',
    'Fidget',
    'Flappy',
    'Guess',
    'Life',
    'Madlibs',
    'Maze',
    'Memory',
    'Minesweeper',
    'Pacman',
    'Paint',
    'Pong',
    'Rps_game',
    'Simonsays',
    'Snake',
    'Tictactoe',
    'Tiles',
    'Tron',
]

def main():
    gamename = 'game name: Tictactoe、Go、Y、Hex、Havannah、snake、paint'
    for game in freegameslist:
        gamename = gamename + '、' + game
        
    parser = argparse.ArgumentParser(
        description="Free_Python_Game & Open_Spiel & Speech_Recognition")
    parser.add_argument('-g', '--game', default='Tictactoe', help=gamename)
    parser.add_argument('-t', '--type', default='mouse', help='mouse or voice')
    parser.add_argument('-s', '--simulations', default=1000,
                        help='How many iterations of MCTS to perform')
    args = parser.parse_args()
    # game_list = ['Tictactoe', 'Go', 'Y', 'Hex', 'Havannah', 'snake', 'paint']
    
    if args.game == 'Tictactoe':
        Tictactoe(args.type, int(args.simulations))
    elif args.game == 'Go':
        Go(args.type, int(args.simulations))
    elif args.game == 'Y':
        Y(args.type, int(args.simulations))
    elif args.game == 'Hex':
        Hex(args.type, int(args.simulations))
    elif args.game == 'Havannah':
        Havannah(args.type, int(args.simulations))
    elif args.game == 'snake':
        freegames_extern.snake.main()
    elif args.game == 'paint':
        freegames_extern.paint.main()
    elif args.game in freegameslist:
        name = '/' + str(args.game).lower() + '.py'
        os.system('python ' + path + name)

if __name__ == '__main__':
    main()
