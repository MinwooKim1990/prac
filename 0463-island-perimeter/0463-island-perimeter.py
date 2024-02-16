class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    # Check the cell to the right
                    if j < cols - 1 and grid[i][j+1] == 1:
                        perimeter -= 2
                    # Check the cell below
                    if i < rows - 1 and grid[i+1][j] == 1:
                        perimeter -= 2
        return perimeter
