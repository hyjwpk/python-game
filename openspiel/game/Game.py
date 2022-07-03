from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from openspiel.algorithms import mcts
from openspiel.bots import human
import pyspiel


class Game():
    def __init__(self, name, show, type='mouse', simulations=1000) -> None:
        self.game = pyspiel.load_game(name)
        self.type = type
        self.bots = [
            self.init_bot('mcts', self.game, simulations),
            self.init_bot('human', self.game),
        ]
        self.state = self.game.new_initial_state()
        self.show = show
        self.init_game()

    def init_bot(self, bot_type, game, simulations=1000):
        """Initializes a bot by type."""
        rng = np.random.RandomState(None)
        if bot_type == "mcts":
            evaluator = mcts.RandomRolloutEvaluator(1, rng)
            return mcts.MCTSBot(
                game,
                2,
                simulations,
                evaluator,
                random_state=rng,
                solve=True,
                verbose=False)
        if bot_type == "human":
            return human.HumanBot(self.type)
        raise ValueError("Invalid bot type: %s" % bot_type)

    def init_game(self):
        print("Initial state:\n{}".format(self.state))
        self.show(str(self.state))
        self.play_game()

    def play_game(self, position=None):
        if self.state.is_terminal():
            return
        current_player = self.state.current_player()
        bot = self.bots[current_player]
        action = bot.step(self.state, position)
        action_str = self.state.action_to_string(current_player, action)
        print("Player {} sampled action: {}".format(
            current_player, action_str))

        for i, bot in enumerate(self.bots):
            if i != current_player:
                bot.inform_action(self.state, current_player, action)
        self.state.apply_action(action)

        print("Next state:\n{}".format(self.state))
        self.show(str(self.state))

        if self.state.is_terminal():
            overall_returns = [0, 0]
            for i, v in enumerate(self.state.returns()):
                overall_returns[i] += v
            print("Overall returns", overall_returns)
