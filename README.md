# GameOfLife
Rule:
A given cell (i, j) in the simulation is accessed on a grid [i][j], where i and j are the row and column indices, respectively. The value of a given cell at a given instant of time depends on the state of its neighbors at the previous time step. Conway’s Game of Life has four rules.<br />
If a cell is alive and has fewer than two neighbors that are alive, it turns dead <br />
If a cell is alive and has either two or three neighbors that are alive, it remains alive.<br />
If a cell is alive and has more than three neighbors that are alive, it turns dead.<br />
If a cell is dead and has exactly three neighbors that are alive, it turns alive.<br />

### Algorithm

1. Initialize the cells in the grid.<br />
2. At each time step in the simulation, for each <br />
   cell (i, j) in the grid, do the following:<br />
   a. Update the value of cell (i, j) based on 
      its neighbors, taking into account the 
      boundary conditions.<br />
   b. Update the display of grid values.<br />
   
resources: 
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life <br />
https://nicholasrui.com/2017/12/18/convolutions-and-the-game-of-life/
