"""
# Dots and Squares

| Import             |`from dots_and_squares import dots_and_squares_v0`|
|--------------------|--------------------------------------------------|
| Actions            | Discrete                                         |
| Parallel API       | No                                               |
| Manual Control     | No                                               |
| Agents             | `agents= ['player_0', 'player_1',...]`           |
| Agents             | n>1                                              |
| Action Shape       | (1,)                                             |
| Action Values      | Discrete((n_rows+1)*n_cols+n_rows*(n_cols+1))    |
| Observation Shape  | TODO                                             |
| Observation Values | TODO                                             |


The Dots and Squares game is a multiplayer game where the players take turns to draw a line on edges of a grig. 
Each time a player places an edge that closes a square, the player gets a point and is allowed to play again. 
The player with the most points (that closed the most squares) at the end of the game wins.

## Coordinate system
The game logic is implemented in the `Dots_and_squares` class in the `backend.py` file, but is explained here.

A grid of `n_rowsxn_cols` squares is represented as a 2D grid with `(n_rows+1)*n_cols` row edges and `n_row*(n_cols+1)` column edges.

### 3x3 grid example

In the following example, the grid is represented as a 3x3 grid with 4*3 row edges and 3*4 column edges:
* Each edge is represented by a tuple (i,j) where i is the row index and j is the column index.
* The row edges are represented by the horizontal lines `---` and their coordinates are located on the left of the line.
* The column edges are represented by the vertical lines `|` and their coordinates are located on the right of the line.

```bash
(0,0)---(0,1)---(0,2)---
|(0,0)   |(0,1)   |(0,2)   |(0,3)
(1,0)---(1,1)---(1,2)---
|(1,0)   |(1,1)   |(1,2)   |(1,3)
(2,0)---(2,1)---(2,2)---
|(2,0)   |(2,1)   |(2,2)   |(2,3)
(3,0)---(3,1)---(3,2)---
```


## Observation Space
TODO

## Action Space
The action space is a Discrete space with the number of possible actions being the number of edges in the grid.

For an n_rowsxn_cols grid, the number of edges is n_rows*(n_cols+1) + n_cols*(n_rows+1).


"""

from pettingzoo import AECEnv
from gymnasium import spaces
from backend import Dots_and_squares

class raw_env(AECEnv):
    metadata = {
        "name": "dots-and-squares_v0",
    }

    def __init__(self, grid_size:tuple = (6,6), n_players:int = 2)->None:
        super().__init__()

        # Backend initialization
        self.grid_size = grid_size
        self.n_players = n_players
        self.game_instance = Dots_and_squares(grid_size = self.grid_size, n_players = self.n_players)

        # RL environment initialization
        self.agents = ["player_" + str(i) for i in range(self.n_players)]

        self.action_spaces = {
            name: spaces.Discrete(
                self.game_instance.rows.size + self.game_instance.columns.size 
            ) for name in self.agents
        }

        self.observation_spaces = {
            name: spaces.Dict(
                {
                "rows": spaces.Box(low=0, high=1, shape=self.game_instance.rows.shape, dtype=int),  # Binary availability of row edges
                "columns": spaces.Box(low=0, high=1, shape=self.game_instance.columns.shape, dtype=int),  # Binary availability of column edges
                "squares": spaces.Box(low=-1, high=self.n_players, shape=self.game_instance.squares.shape, dtype=int)  # Ownership of squares, might not be relevant
                }
            ) for name in self.agents
        }

        # Rendering initialization
        self.render_mode = "human"

    def reset(self)->None:
        """
        This method resets the environment to its initial state.
        """
        self.game_instance = Dots_and_squares(grid_size = self.grid_size, n_players = self.n_players)

    def step(self, actions):
        # TODO: Implement this method
        pass

    def render(self):
        # TODO: Implement this method
        pass

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]
    
    def check_game_over(self):
        return self.game_instance.is_game_over()
    
    def interpret_action(self, action):

        total_row_edges = self.game_instance.rows.size

        if action < total_row_edges:
            # Row edge
            row = action // self.game_instance.n_cols
            col = action % n_cols
            return ("r", (row, col))
        else:
            # Column edge
            action -= total_row_edges
            row = action // (n_cols + 1)
            col = action % (n_cols + 1)
            return ("c", (row, col))


if __name__ == "__main__":
    env = raw_env(grid_size  = (6,6), n_players  = 3)
    print(env.agents)
    print(env.action_spaces)
    #env.reset()
    #env.step([0, 1])
    #env.render()
    #env.close()