class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return spiralTraversal(matrix)
        
        
def spiralTraversal(arr):
    return spiralTraversalHelper(arr, 0, 0, len(arr)-1, len(arr[0])-1)

def spiralTraversalHelper(arr, sr, sc, er, ec):
    res = []

    while sr <=er and sc <= ec:
        # Top row
        for col in range(sc, ec+1):
            #print('first')
            res.append(arr[sr][col])
        sr+=1

        # Right col
        for row in range(sr, er+1):
            #print('second')
            res.append(arr[row][ec])
        ec-=1

        # bottom row
        if sr <=er:
            for col in reversed(range(sc, ec-1)):
            
                #print('third')
                res.append(arr[er][col])
            er-=1

        # left col
        if sc<=ec:
            for row in reversed(range(sr+1, er-1)):
                #print('fourth')
                res.append(arr[row][sc])
            sc+=1


        
    return res

