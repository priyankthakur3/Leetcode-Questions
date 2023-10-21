class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        prev_color = image[sr][sc]

        def dfs_helper(x, y):
            # check if x and y are within bounds of image and image[x][y] == prev_color
            # if not then return stack
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == prev_color:
                image[x][y] = color
            else:
                return

            # start recursion for all 4 direction
            for tx, ty in directions:
                dfs_helper(x + tx, y + ty)

        dfs_helper(sr, sc)
        return image
