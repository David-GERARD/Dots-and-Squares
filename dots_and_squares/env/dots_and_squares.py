from pettingzoo import AECEnv
from backend import Dots_and_squares

class raw_env(AECEnv):
    metadata = {
        "name": "dots-and-squares_v0",
    }

    def __init__(self, grid_size=(3,3), n_players=2):
        self.game_instance = Dots_and_squares(grid_size=grid_size, n_players=n_players)

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

if __name__ == "__main__":
    env = raw_env()
    #env.reset()
    #env.step([0, 1])
    #env.render()
    #env.close()