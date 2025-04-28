# Backtracking for N-Queens
def solve_n_queens_backtracking(n):
    board = [-1] * n  # board[i] = column position of queen in row i
    solutions = []

    def is_safe(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or \
               abs(board[prev_row] - col) == abs(prev_row - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # backtrack

    backtrack(0)
    return solutions

# Example usage
n = 4
solutions = solve_n_queens_backtracking(n)
print(f"Solutions using Backtracking for {n}-Queens:")
for sol in solutions:
    print(sol)


#____________________________________________________

#Branch and Bound:-

# Branch and Bound for N-Queens
def solve_n_queens_branch_and_bound(n):
    board = [-1] * n
    solutions = []

    column = [False] * n
    diag1 = [False] * (2*n-1)  # r+c
    diag2 = [False] * (2*n-1)  # r-c+n-1

    def place_queen(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if not column[col] and not diag1[row+col] and not diag2[row-col+n-1]:
                board[row] = col
                column[col] = diag1[row+col] = diag2[row-col+n-1] = True
                place_queen(row + 1)
                # Undo (backtrack)
                column[col] = diag1[row+col] = diag2[row-col+n-1] = False
                board[row] = -1

    place_queen(0)
    return solutions

# Example usage
n = 4
solutions = solve_n_queens_branch_and_bound(n)
print(f"\nSolutions using Branch and Bound for {n}-Queens:")
for sol in solutions:
    print(sol)

