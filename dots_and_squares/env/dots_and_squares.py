from pettingzoo import AECEnv
from backend import Dots_and_squares

class raw_env(AECEnv):
    metadata = {
        "name": "dots-and-squares_v0",
    }

    def __init__(self):
        self.game_instance = Dots_and_squares()

    def reset(self, seed=None, options=None):
        pass

    def step(self, actions):
        pass

    def render(self):
        pass

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]
