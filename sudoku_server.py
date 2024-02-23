import json


json_sudoku_arr = '[[5, 3, 0, 0, 7, 0, 0, 0, 0],[6, 0, 0, 1, 9, 5, 0, 0, 0],[0, 9, 8, 0, 0, 0, 0, 6, 0],[8, 0, 0, 0, 6, 0, 0, 0, 3],[4, 0, 0, 8, 0, 3, 0, 0, 1],[7, 0, 0, 0, 2, 0, 0, 0, 6],[0, 6, 0, 0, 0, 0, 2, 8, 0],[0, 0, 0, 4, 1, 9, 0, 0, 5],[0, 0, 0, 0, 8, 0, 0, 7, 9]]'
                

python_sudoku_arr = json.loads(json_sudoku_arr)
print(python_sudoku_arr)
print(type(python_sudoku_arr))



def sudoku_verifier(sudoku_grid):
    #creates lists of 9 empty sets
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = [set() for _ in range(9)]

    #loop over grid
    for i in range(9):
        for j in range(9):
            #get num in current cell
            num = sudoku_grid[i][j]
            if num == 0:
                continue
            
            #calculate the index of the 3x3 subgrid where the current cell is located
            subgrid_index = (i // 3) * 3 + j // 3
            
            #if current num is already in the grid, return false
            if num in rows[i] or num in cols[j] or num in subgrids[subgrid_index]:
                return 0

            #add the num
            rows[i].add(num)
            cols[j].add(num)
            subgrids[subgrid_index].add(num)

    return 1


if sudoku_verifier(python_sudoku_arr):
    print('Pass')
else:
    print('fail')
