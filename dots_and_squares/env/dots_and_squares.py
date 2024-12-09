from pettingzoo import AECEnv
from backend import Dots_and_squares

class raw_env(AECEnv):
    metadata = {
        "name": "dots-and-squares_v0",
    }

    def __init__(self, grid_size:tuple = (6,6), n_players:int = 2)->None:
        super().__init__()
        self.grid_size = grid_size
        self.n_players = n_players
        self.game_instance = Dots_and_squares(grid_size = self.grid_size, n_players = self.n_players)

    def reset(self)->None:
        """
        This method resets the environment to its initial state.
        """
        self.game_instance = Dots_and_squares(grid_size = self.grid_size, n_players = self.n_players)

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