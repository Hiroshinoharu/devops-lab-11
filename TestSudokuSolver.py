import unittest
from SudokuSolver import solve_sudoku

class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self.valid_puzzle_1 = [
            0, 0, 4, 0, 5, 0, 0, 0, 0,
            9, 0, 0, 7, 3, 4, 6, 0, 0,
            0, 0, 3, 0, 2, 1, 0, 4, 9,
            0, 3, 5, 0, 9, 0, 4, 8, 0,
            0, 9, 0, 0, 0, 0, 0, 3, 0,
            0, 7, 6, 0, 1, 0, 9, 2, 0,
            3, 1, 0, 9, 7, 0, 2, 0, 0,
            0, 0, 9, 1, 8, 2, 0, 0, 3,
            0, 0, 0, 0, 6, 0, 1, 0, 0
        ]
        self.valid_puzzle_2 = [
            8, 0, 0, 1, 0, 7, 4, 6, 9,
            0, 0, 5, 3, 0, 6, 0, 8, 0,
            0, 0, 0, 0, 0, 4, 0, 3, 5,
            9, 8, 0, 0, 7, 0, 0, 1, 0,
            2, 5, 7, 8, 3, 0, 0, 9, 0,
            0, 1, 0, 0, 0, 0, 8, 7, 2,
            0, 0, 8, 0, 0, 0, 9, 0, 0,
            4, 2, 0, 7, 0, 3, 1, 0, 0,
            0, 6, 1, 9, 0, 0, 3, 0, 0
        ]
        self.valid_puzzle_3 = [
            0,1,5,6,0,7,0,3,4,
            0,2,7,0,0,0,0,5,0,
            6,8,0,0,0,4,7,1,0,
            5,0,0,1,0,0,4,0,0,
            0,3,0,0,7,0,0,0,8,
            0,0,4,0,0,8,9,2,0,
            3,0,9,7,0,6,1,0,5,
            0,0,6,8,9,1,3,0,0,
            0,7,0,3,0,5,0,0,0
        ]
        self.valid_puzzle_4 = [
            3, 0, 2, 0, 8, 0, 1, 0, 5,
            0, 0, 7, 2, 0, 0, 0, 6, 0,
            5, 0, 8, 9, 0, 0, 0, 4, 7,
            0, 8, 0, 4, 0, 0, 3, 0, 2,
            0, 3, 0, 1, 6, 0, 0, 5, 8,
            0, 1, 0, 5, 0, 0, 6, 7, 0,
            0, 2, 0, 3, 4, 5, 0, 0, 1,
            0, 0, 0, 0, 2, 6, 0, 0, 9,
            0, 0, 0, 0, 9, 0, 5, 2, 6
        ]
        self.valid_puzzle_5 = [
            0, 3, 1, 6, 7, 0, 4, 0, 9,
            0, 0, 0, 8, 3, 0, 0, 0, 0,
            8, 2, 0, 0, 0, 0, 0, 1, 0,
            0, 7, 4, 0, 0, 8, 1, 6, 0,
            0, 8, 0, 0, 6, 0, 0, 0, 4,
            9, 0, 2, 0, 0, 0, 0, 7, 3,
            4, 9, 0, 0, 5, 7, 2, 3, 0,
            2, 0, 0, 0, 9, 0, 5, 0, 7,
            7, 0, 3, 2, 0, 0, 6, 0, 1
        ]
        self.unsolvable_puzzle = [
            5, 1, 6, 8, 4, 9, 7, 3, 2,
            3, 0, 7, 6, 0, 5, 0, 0, 0,
            8, 0, 9, 7, 0, 0, 0, 6, 5,
            1, 3, 5, 0, 6, 0, 9, 0, 7,
            4, 7, 2, 5, 9, 0, 0, 0, 6,
            9, 6, 8, 3, 7, 2, 0, 0, 4,
            2, 5, 3, 1, 8, 6, 4, 7, 9,
            6, 8, 4, 0, 5, 0, 3, 0, 0,
            7, 0, 0, 0, 0, 0, 8, 5, 0
        ]

    def test_solve_valid_puzzle(self):
        result = solve_sudoku(self.valid_puzzle_1)
        expected_solution = [
            2, 6, 4, 8, 5, 9, 3, 1, 7,
            9, 8, 1, 7, 3, 4, 6, 5, 2,
            7, 5, 3, 6, 2, 1, 8, 4, 9,
            1, 3, 5, 2, 9, 7, 4, 8, 6,
            8, 9, 2, 5, 4, 6, 7, 3, 1,
            4, 7, 6, 3, 1, 8, 9, 2, 5,
            3, 1, 8, 9, 7, 5, 2, 6, 4,
            6, 4, 9, 1, 8, 2, 5, 7, 3,
            5, 2, 7, 4, 6, 3, 1, 9, 8
        ]
        self.assertEqual(result, expected_solution)
        
    def test_solve_valid_puzzle_2(self):
        result = solve_sudoku(self.valid_puzzle_2)
        expected_solution = [
            8, 3, 2, 1, 5, 7, 4, 6, 9,
            7, 4, 5, 3, 9, 6, 2, 8, 1,
            1, 9, 6, 2, 8, 4, 7, 3, 5,
            9, 8, 4, 6, 7, 2, 5, 1, 3,
            2, 5, 7, 8, 3, 1, 6, 9, 4,
            6, 1, 3, 5, 4, 9, 8, 7, 2,
            3, 7, 8, 4, 1, 5, 9, 2, 6,
            4, 2, 9, 7, 6, 3, 1, 5, 8,
            5, 6, 1, 9, 2, 8, 3, 4, 7
        ]
        self.assertEqual(result, expected_solution)
        
    def test_solve_valid_puzzle_3(self):
        result = solve_sudoku(self.valid_puzzle_3)
        expected_solution = [
            9,1,5,6,8,7,2,3,4,
            4,2,7,9,1,3,8,5,6,
            6,8,3,2,5,4,7,1,9,
            5,9,8,1,6,2,4,7,3,
            1,3,2,4,7,9,5,6,8,
            7,6,4,5,3,8,9,2,1,
            3,4,9,7,2,6,1,8,5,
            2,5,6,8,9,1,3,4,7,
            8,7,1,3,4,5,6,9,2
        ]
        self.assertEqual(result, expected_solution)
        
    def test_solve_valid_puzzle_4(self):
        result = solve_sudoku(self.valid_puzzle_4)
        expected_solution = [
            3,4,2,6,8,7,1,9,5,
            1,9,7,2,5,4,8,6,3,
            5,6,8,9,1,3,2,4,7,
            6,8,5,4,7,9,3,1,2,
            7,3,4,1,6,2,9,5,8,
            2,1,9,5,3,8,6,7,4,
            9,2,6,3,4,5,7,8,1,
            8,5,1,7,2,6,4,3,9,
            4,7,3,8,9,1,5,2,6
        ]
        self.assertEqual(result, expected_solution)
        
    def test_solve_valid_puzzle_5(self):
        result = solve_sudoku(self.valid_puzzle_5)
        expected_solution = [
            5,3,1,6,7,2,4,8,9,
            6,4,9,8,3,1,7,5,2,
            8,2,7,5,4,9,3,1,6,
            3,7,4,9,2,8,1,6,5,
            1,8,5,7,6,3,9,2,4,
            9,6,2,4,1,5,8,7,3,
            4,9,6,1,5,7,2,3,8,
            2,1,8,3,9,6,5,4,7,
            7,5,3,2,8,4,6,9,1
        ]
        self.assertEqual(result, expected_solution)

    def test_unsolvable_puzzle(self):
        with self.assertRaises(ValueError):
            solve_sudoku(self.unsolvable_puzzle)

if __name__ == "__main__":
    unittest.main()