class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points
        
        dist = [(x*x + y*y, [x, y]) for x, y in points]
        dist.sort()
        return [p for d, p in dist[:k]]
