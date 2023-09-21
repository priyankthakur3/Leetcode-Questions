class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        
        finalOutput = []
        i , j , flag = 0, 0 , 1
       
        for _ in range(m*n):
            finalOutput.append(mat[i][j])
            if flag == 1:
                if i == 0 and j != n-1:
                    j += 1
                    flag = 0
                elif j == n - 1:
                    i += 1
                    flag = 0   
                else:
                    i -= 1
                    j += 1  
            else:
                if j == 0 and i != m - 1:
                    i += 1
                    flag = 1
                elif i == m - 1:
                    j += 1
                    flag = 1
                else:
                    i += 1
                    j -= 1
        return finalOutput
