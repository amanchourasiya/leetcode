class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start = 0
        end = len(A)-1

        while start < end :
            while A[start] & 1  == 0:
                start+=1

            while A[end] & 1 == 1:
                end-=1
            
            A[start], A[end] = A[end], A[start]
        
        return A
