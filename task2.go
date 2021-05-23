package main

import (
	"fmt"
)

func main() {
	matrix := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}

	newMatrix := RotateMatrix(matrix)
	fmt.Printf("%v\n", newMatrix)
}

func RotateMatrix(matrix [][]int) [][]int {
	// Rotate the matrix with main diagonal as axis
	length := len(matrix)
	for i := 0; i < length; i++ {
		for j := 0; j < i; j++ {
			tmp := matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = tmp
		}

	}

	for i := 0; i < length; i++ {
		for j := 0; j < length/2; j++ {
			tmp := matrix[i][j]
			matrix[i][j] = matrix[i][length-j-1]
			matrix[i][length-j-1] = tmp
		}
	}
	return matrix
}
