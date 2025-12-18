class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    x1,y1 = points[i]
                    x2,y2 = points[j]
                    x3,y3 = points[k]

                    temp = 0.5 * (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
                    area = max(area,temp)
        return area