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
    
   
def validate_grid(grid : list)->bool:
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
            if not(validate_grid(subgrid)):
                return False            
    
    all_values = set()
    cols_values = dict()
    for row_index,row in enumerate(grid):
        row_values = set()       
        for col_index,cell_value in enumerate(row):
            if is_sub_grid:
                if(cell_value in all_values):
                    return False
                all_values.add(cell_value)
            # row
            if cell_value in row_values:             
                return False
            row_values.add(cell_value) 
            # col
            if not(col_index in cols_values.keys()):
                cols_values.update({col_index:set()})
            else:
                if(cell_value in cols_values.get(col_index)):
                    return False 
            cols_values.get(col_index).add(cell_value)
               
    return True

def validate_row(row:list):
    return False

def fill_grid(grid : list) -> list:
    
    print_grid(grid)
    
    sub_grids = get_sub_grids(grid)
    for sub_grid in sub_grids:
        print_grid(sub_grid)
    
    
    # for row in grid:
    #     print(current_grid)
    
    
    
    return list()
    
    
    
testing_grid = incomplete_grid_01
filled_grid = fill_grid(testing_grid)

# print_grid(testing_grid)    
# if validate_grid(testing_grid):
#     print ("The grid is valid",end="\n\n------------\n")
# else:
#     print("The grid is invalid",end="\n\n-------------\n")   
    
    
    
    
    
