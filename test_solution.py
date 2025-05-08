import unittest
from solution import Solution

class TestSurroundedRegions(unittest.TestCase):
    def setUp(self):
        self.solution = Solution() 
    
    def test_basic_case(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_no_change_needed(self):
        board = [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ]
        expected = [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_edge_case_no_surrounded_regions(self):
        board = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"]
        ]
        expected = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)


if __name__ == '__main__':
    unittest.main()