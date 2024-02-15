class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second to last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # For each element, add the minimum of the two possible paths leading to it from below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
        # The top element now contains the minimum path sum
        return triangle[0][0]
