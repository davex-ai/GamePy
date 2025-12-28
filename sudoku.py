def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return puzzle[r][c]
    return None, None

def is_valid(puzzle, guess, row, col):
    row_val = puzzle[row]
    if guess in row_val:
        return False
    col_val = [puzzle[i][col] for i in range(9)]
    if guess in col_val:
        return False

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
    if row is None:
        return  True
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):