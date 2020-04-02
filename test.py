import unittest
from gameoflife import Life
import numpy as numpy

class Testlife(unittest.TestCase):
	def setUp(self):
	    self.game = Life()

	def test_valid(self):
	    self.assertTrue(self.game.select('blinker'))
	
	def test_invalid(self):
	    self.assertFalse(self.game.select(''))

	def test_case(self):
	    self.assertTrue(self.game.select('Beacon'))
	    self.assertTrue(self.game.select('toad'))
	    self.assertTrue(self.game.select('GLIDER'))

	def test_no_selection(self):
	    self.assertIsNone(self.game.get_board())

class TestConfigs(unittest.TestCase):
   
    def setUp(self):
        self.game = Life()
    
    def two_steps(self, pattern, board1, board2):
        self.game.select(pattern)
        init_board = self.game.get_board()
        np.testing.assert_array_equal(init_board, board1)

        self.game.update()
        np.testing.assert_array_equal(self.game.get_board(), board2)

        self.game.update()
        np.testing.assert_array_equal(self.game.get_board(), init_board)

    def test_blinker(self):
        self.two_steps('blinker', np.array(
            [[0,0,0,0,0],
            [0,1,1,1,0],
            [0,0,0,0,0]], dtype=np.uint8), np.array(
                [[0,0,1,0,0],
                [0,0,1,0,0],
                [0,0,1,0,0]], dtype=np.uint8))

    def test_toad(self):
        self.two_steps('toad', np.array(
            [[0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]], dtype=np.uint8), np.array(
                [[0, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 0]], dtype=np.uint8))

    def test_beacon(self):
        self.two_steps('beacon', np.array(
            [[1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]], dtype=np.uint8), np.array(
                [[1, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 1]], dtype=np.uint8))


class TestConfig(unittest.TestCase):
    
    def setUp(self):
        self.game = Life()

    def multiple_steps(self, pattern, *boards):
        self.game.select(pattern)
        init_board = self.game.get_board()

        np.testing.assert_array_equal(init_board, boards[0])

        for board in boards[1:]:
            self.game.update()
            np.testing.assert_array_equal(self.game.get_board(), board)

    def test_glider(self):
        board1 = np.array(
            [[1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)
        
        board2 = np.array(
            [[0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)

        board3 = np.array(
            [[0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)

        self.multiple_steps('glider', board1, board2, board3)




if __name__ == 'main':
	unittest.main()