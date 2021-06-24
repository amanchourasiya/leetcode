def squareOfZeroes(matrix):
    newMatrix = createHelperMatrix(matrix)
    print(newMatrix)
    l = len(matrix)
    res = False
    for row in range(l):
        if res:
            break
        for col in range(l):
            if matrix[row][col] != 1:
                down, right = newMatrix[row][col]
                down = min(down, right)
                if newMatrix[row][col+down-1][0] >= down and newMatrix[row+down-1][col][1] >= down:
                    res = True
                    break
    return res


def createHelperMatrix(matrix):
    l = len(matrix)
    newMatrix = [[(0,0) for _ in range(l)] for _ in range(l)]

    for row in range(l-1, -1, -1):
        for col in range(l-1, -1, -1):
            if matrix[row][col] != 1:
                right = 1
                down = 1
                if row < l-1:
                    down = 1 + newMatrix[row+1][col][0]
                if col < l-1:
                    right = 1 + newMatrix[row][col+1][1]

                newMatrix[row][col] = (down, right)

    return newMatrix

mat = [[1,1,1,0,1,0],
    [0,0,0,0,0,1],
    [0,1,1,1,0,1],
    [0,0,0,1,0,1],
    [0,1,1,1,0,1],
    [0,0,0,0,0,1]]

print(squareOfZeroes(mat))

# time O(n^2) | space O(n^2)