# GameOfLife
Rule:
A given cell (i, j) in the simulation is accessed on a grid [i][j], where i and j are the row and column indices, respectively. The value of a given cell at a given instant of time depends on the state of its neighbors at the previous time step. Conway’s Game of Life has four rules.
If a cell is ON and has fewer than two neighbors that are ON, it turns OFF <br />
If a cell is ON and has either two or three neighbors that are ON, it remains ON.<br />
If a cell is ON and has more than three neighbors that are ON, it turns OFF.<br />
If a cell is OFF and has exactly three neighbors that are ON, it turns ON.<br />

### Algorithm

1. Initialize the cells in the grid.<br />
2. At each time step in the simulation, for each <br />
   cell (i, j) in the grid, do the following:<br />
   a. Update the value of cell (i, j) based on 
      its neighbors, taking into account the 
      boundary conditions.<br />
   b. Update the display of grid values.<br />
   
   source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
