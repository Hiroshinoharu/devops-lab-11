numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def options(cell, sudoku):
    """Determine the degree of freedom for a cell."""
    column = {sudoku[ix] for ix in range(cell % 9, 81, 9)}
    row = {sudoku[ix] for ix in range((cell // 9) * 9, (cell // 9) * 9 + 9)}
    box = {
        sudoku[ix]
        for ix in range(81)
        if (ix // 27 == cell // 27) and (ix % 9 // 3 == cell % 9 // 3)
    }
    return numbers - (box | row | column)

def solve_sudoku(sudoku):
    if len(sudoku) != 81:
        raise ValueError("Invalid Sudoku grid size.")
    
    job_queue = [sudoku[:]]  # Copy the initial state to avoid mutating it.

    while job_queue:
        state = job_queue.pop(0)
        if not any(i == 0 for i in state):  # If no missing values, solved.
            return state

        # Determine the degrees of freedom for each cell.
        degrees_of_freedom = [
            0 if v != 0 else len(options(ix, state)) for ix, v in enumerate(state)
        ]

        if all(v == 0 for v in degrees_of_freedom):
            raise ValueError("Puzzle is unsolvable.")

        # Find the cell with the least freedom.
        least_freedom = min(v for v in degrees_of_freedom if v > 0)
        cell = degrees_of_freedom.index(least_freedom)

        for option in options(cell, state):
            new_state = state[:]
            new_state[cell] = option
            job_queue.append(new_state)

    return state