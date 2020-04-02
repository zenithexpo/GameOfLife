import scipy.signal 
import numpy as np
import json

cfile = "config.json"

class Life:
    def __init__(self):
        with open(cfile) as f:
            data = f.read()
        
        self.patterns = json.loads(data)     
        self.cur_board = None
        self.iters = 0
        self.alive = 0
        self.pattern_name = None
        self.nextgrid=[]

    def lstPatterns(self):
        return self.patterns

    def select(self, pattern_name):
        if pattern_name.lower() not in self.patterns:
            return False 
        else:
            self.pattern_name = pattern_name
            self.cur_board = np.array(self.patterns[pattern_name.lower()], dtype=np.uint8)
            self.alive = 0
            self.iters = 0
            return True

    def applyRule(self):
        conv = np.ones((3,3), dtype=np.uint8)
        if self.cur_board is None:
            return False 

        new_board = scipy.signal.convolve2d(self.cur_board, conv, mode="same")

        (m, n) = self.cur_board.shape
        for i in range(m):
            for j in range(n):
                if new_board[i,j] == 3:
                    new_board[i, j] = 1
                elif new_board[i, j] == 4:
                    new_board[i, j] = self.cur_board[i, j]
                else:
                    new_board[i, j] = 0

        self.cur_board = new_board
        self.iters += 1
        self.alive = sum(sum(self.cur_board))
        return True
 
    def get_board(self):
        return self.cur_board

