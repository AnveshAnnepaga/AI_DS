def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if len(set(row)) != 9:
            return False
    
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if len(set(column)) != 9:
            return False

    # Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = []
            for r in range(i, i+3):
                for c in range(j, j+3):
                    block.append(board[r][c])
            if len(set(block)) != 9:
                return False
    return True


# Example grid
sudoku = [
   [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


print("Sudoku is valid:", is_valid_sudoku(sudoku))
