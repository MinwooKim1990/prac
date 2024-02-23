from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        # Initialize the triangle with the first row
        triangle = [[1]]
        
        for i in range(1, numRows):
            # Start each row with a 1
            row = [1]
            # Compute the in-between values for the row
            for j in range(1, i):
                # Each new entry is the sum of the two above it
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # End each row with a 1
            row.append(1)
            # Add the completed row to the triangle
            triangle.append(row)
        
        return triangle     