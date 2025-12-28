def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return puzzle[r][c]
    return None, None

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
