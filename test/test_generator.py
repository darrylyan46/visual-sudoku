from sudoku import generator
import unittest

class TestGenerator(unittest.TestCase):
    """
    Unit testing for the visual-sudoku generator library.
    """

    def testCreateEmptyGrid(self):
        self.assertEqual(generator.createEmptyGrid(), [[None for _ in range(3)] for _ in range(3)])
        self.assertEqual(generator.createEmptyGrid(2), [[None, None], [None, None]])
        self.assertRaises(ValueError, generator.createEmptyGrid, -1)
