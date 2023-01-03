from math import dist
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [sum(dist(p,(c[0],c[1]))<=c[2] for p in points) for c in queries]
