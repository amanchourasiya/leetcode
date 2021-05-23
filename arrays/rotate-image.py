class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # reverse up down
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-i-1], matrix[i]

        # mirror matrix diagonally
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
