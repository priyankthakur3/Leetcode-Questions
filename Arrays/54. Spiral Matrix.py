class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top, left, bottom, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        traverseList = []

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                traverseList.append(matrix[top][i])
            top += 1
            
            if top <= bottom and left <= right:
                for j in range(top, bottom + 1):
                    traverseList.append(matrix[j][right])
                right -= 1

            if top <= bottom and left <= right:
                for i in range(right, left - 1, -1):
                    traverseList.append(matrix[bottom][i])
                bottom -= 1
            if top <= bottom and left <= right:
                for j in range(bottom, top - 1 , -1):
                    traverseList.append(matrix[j][left])
                left += 1
        return traverseList
                