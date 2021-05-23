# Directions

dirs = [
    [0,-1], # UP
    [-1,0],  # LEFT
    [0,1], # DOWN
    [1,0]   # RIGHT
]

def dfs(grid, x0, y0, i,j, v):
    rows = len(grid)
    cols = len(grid[0])

    if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] <=0:
        return

    # Marking current point as visited
    grid[i][j] *= -1

    # Computing the coordinates with x0, y0 as base
    v.append((i-x0, j-y0))

    # Traverse in all directions
    for d in dirs:
        dfs(grid, x0, y0, i + d[0], j+ d[1], v)

def countIslands(grid):
    rows = len(grid)
    if rows == 0:
        return 0

    cols = len(grid[0])
    if cols == 0:
        return 0

    coordinates = set()

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 1:
                continue
            v = []
            dfs(grid, row, col, row, col, v)
            coordinates.add(tuple(v))

    return len(coordinates)

grid = [[ 1, 1, 0, 1, 1 ],
[ 1, 0, 0, 0, 0 ],
[ 0, 0, 0, 0, 1 ],
[ 1, 1, 0, 1, 1 ] ]

print(countIslands(grid))

