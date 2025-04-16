def is_valid(sudoku, num, spot):
    line, column = spot
    #First check in line
    for j in range(9):
        if sudoku[line][j] == num and column != j:
            return False

    #Second check in column
    for i in range(9):
        if sudoku[i][column] == num and line != i:
            return False
    
    #Then check in subgrid
    init_line = line - (line % 3)
    init_column = column - (column % 3)
    for i in range(3):
        for j in range(3):
            if sudoku[init_line + i][init_column + j] == num and (init_line + i,init_column + j) != spot:
                return False
    # The number is valid        
    return True

def find_empty_cell(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i,j)
    return None

def solve_sudoku(sudoku):
    # Look for empty cells (represented by 0)
    empty = find_empty_cell(sudoku)
    if not empty:
          return True
    
    line, column = empty

    # Test numbers from 1 thrue 9 in empty spot
    for num in range(1, 10):
        if is_valid(sudoku, num, (line, column)):
            sudoku[line][column] = num # Try with number
            if solve_sudoku(sudoku): #Recursivity 
                return True # Sudoku done!
            
            sudoku[line][column] = 0 # Set back zero and try again (backtrack)

    return False

def print_sudoku(sudoku):
    # Print a nice board
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(sudoku[i][j], end=" ")
        print()

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
    # Print unsolved board
    print('Unsolved board\n')
    print_sudoku(sudoku)
    print('\n')

    # Solve the Sudoku puzzle
    if solve_sudoku(sudoku):
        print('Sudoku solved successfully!\n')
        print_sudoku(sudoku)

    else:
        print("No solution exists.")