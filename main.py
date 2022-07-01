import argparse
from Tictactoe import Tictactoe
from Go import Go
from Y import Y
from Hex import Hex
from Havannah import Havannah


def main():
    parser = argparse.ArgumentParser(
        description="Free_Python_Game & Open_Spiel & Speech_Recognition")
    parser.add_argument('-g', '--game', default='Tictactoe', help='game name')
    parser.add_argument('-t', '--type', default='mouse', help='mouse or voice')
    parser.add_argument('-s', '--simulations', default=1000,
                        help='How many iterations of MCTS to perform')
    args = parser.parse_args()
    game_list = ['Tictactoe', 'Go', 'Y', 'Hex', 'Havannah']
    if not args.game in game_list:
        print(game_list)
        exit(-1)
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


if __name__ == '__main__':
    main()
