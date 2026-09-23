valid_grid = [
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
invalid_grid_med = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 8, 6, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]
invalid_grid = [
    [3, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 3, 8, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]  

incomplete_grid_01 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
incomplete_grid_02 = [
    [0, 0, 4, 5, 3, 0, 2, 7, 1],
    [2, 0, 1, 8, 0, 4, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 6, 0],
    [3, 0, 0, 7, 0, 0, 0, 0, 5],
    [6, 4, 0, 0, 9, 2, 0, 0, 0],
    [0, 1, 0, 0, 0, 5, 0, 9, 2],
    [0, 8, 6, 0, 5, 3, 9, 0, 7],
    [0, 2, 0, 1, 8, 6, 0, 5, 0],
    [4, 0, 0, 9, 0, 0, 0, 0, 0],
]
incomplete_grid_03 = [
    [0, 6, 0, 5, 0, 9, 0, 0, 1],
    [2, 0, 0, 0, 0, 0, 0, 3, 0],
    [5, 0, 0, 0, 0, 1, 0, 0, 0],
    [3, 9, 2, 0, 0, 0, 6, 0, 5],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 0, 0, 5, 3, 9, 0],
    [0, 8, 6, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 1, 8, 6, 0, 5, 0],
    [0, 5, 0, 9, 2, 0, 1, 8, 0],
]

def print_grid(grid: list):
    print("\n")
    horiz_sep = ""
    visual_width = (len(grid)*3) + 4 if len(grid) == 9 else (len(grid)*3) + 2    
    for _ in range(visual_width):
        horiz_sep += "-"
        
    for line_index,line in enumerate(grid):
        if(line_index % 3 == 0):            
            print(horiz_sep)
        line_str = "";
        for cell_index, cell in enumerate(line):
           if(cell_index % 3 == 0):
               line_str += "| "
           else:
               line_str += " "
           line_str += str(cell) + " "
        line_str += "|"
        print(line_str) 
    print(horiz_sep)       
    print("\n")
      
def get_sub_grids(grid: list) -> list:
    result = []
    if len(grid) != 9:
        return False
    for start_row in range(0,9,3):
        for start_col in range(0,9,3):
            sub_grid = []
            for row_index in range(start_row,start_row + 3):
                sub_grid.append(grid[row_index][start_col:start_col + 3])
            result.append(sub_grid)
    return result             

def is_valid_value(grid, row, col, value):
    """ 
    check a value can be inserted in the sodoku grid.
    """

    if value in grid[row]:
        return False

    for grid_row in grid:
        if grid_row[col] == value:
            return False    

    sub_grid_row_start = (row // 3) * 3 
    sub_grid_row_end = sub_grid_row_start + 3
    sub_grid_col_start = (col // 3) * 3 
    sub_grid_col_end = sub_grid_col_start + 3    
    for sub_grid_row in grid[sub_grid_row_start:sub_grid_row_end]:
        for cell_value in sub_grid_row[sub_grid_col_start:sub_grid_col_end]:
            if cell_value == value:
                return False

    return True  
   
def validate_grid(grid : list, allow_zero : bool = False)->bool:
    """ 
    check a sodoku grid is valid.
    
    :param grid: the grid to validate.
    :type grid: list of lists
    :return: True if the grid is valid, False if the grid is invalid.
    :rtype: bool
    """
    
    # validate sub grids
    is_sub_grid = len(grid) != 9
    if(not(is_sub_grid)):
        for subgrid in get_sub_grids(grid):
            if not(validate_grid(subgrid, allow_zero)):
                return False            
    
    all_values = set()
    cols_values = dict()
    for row in grid:
        row_values = set()       
        for col_index,cell_value in enumerate(row):

            if allow_zero and cell_value == 0:
                continue

            if is_sub_grid:
                if(cell_value in all_values):
                    # print("sub grid ")
                    return False
                all_values.add(cell_value)
            # row
            if cell_value in row_values:      
                # print(f"row, cell value {cell_value}")       
                return False
            row_values.add(cell_value) 
            # col
            if not(col_index in cols_values.keys()):
                cols_values.update({col_index:set()})
            else:
                if(cell_value in cols_values.get(col_index)):
                    # print("col")
                    return False 
            cols_values.get(col_index).add(cell_value)
               
    return True

def find_empty_cell(grid:list)->tuple:
    for row_index,row in enumerate(grid):
        for col_index,cell in enumerate(row):
            if cell == 0:                
                return (row_index,col_index)


    
def fill_grid(grid : list) -> list:
    
    empty_cell_row_col = find_empty_cell(grid)   

    if empty_cell_row_col is None:
        return grid
    else:
        row, col = empty_cell_row_col
        for value in range(1,10):
            if(is_valid_value(grid,row,col,value)):
                grid[row][col] = value
                # print_grid(grid)
                result = fill_grid(grid)
                if result != None:
                    return result            
                grid[row][col] = 0                           

            # grid[row][col] = value
            # if validate_grid(grid, True):
            #     result = fill_grid(grid)
            #     if result:
            #         return result
            # grid[row][col] = 0           
    return None
    
    
    
testing_grid = incomplete_grid_01
print_grid(testing_grid)
# row = int(input("row : "))
# col = int(input("col : "))
# value = int(input("value : "))
# print(is_valid_value(testing_grid,row,col,value))

filled_grid = fill_grid(testing_grid)
if(filled_grid):
    print_grid(filled_grid)
else:
    print("No solution for this grid")

# print_grid(testing_grid)    
# if validate_grid(testing_grid, True):
#     print ("The grid is valid",end="\n\n------------\n")
# else:
#     print("The grid is invalid",end="\n\n-------------\n")   
    
    
    
    
    
