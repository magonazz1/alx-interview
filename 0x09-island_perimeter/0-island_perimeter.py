def island_perimeter(grid):
    '''
    func: island_perimeter
        returns the perimeter of the island described in grid
    args:
        <list of list of ints: grid> : binary matrix representation of the island
    return:
        <int>
    '''
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter

