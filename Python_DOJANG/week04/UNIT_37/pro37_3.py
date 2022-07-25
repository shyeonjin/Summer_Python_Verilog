# 심사문제: 두 점 사이의 거리 구하기
# 표준 입력 x,y 4개의 좌표입력

import math
class Point2D:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y


length = 0.0 
p = [Point2D(), Point2D(), Point2D(), Point2D()] 
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

length += math.sqrt((p[1].x - p[0].x) ** 2 + (p[1].y - p[0].y) ** 2)
length += math.sqrt((p[2].x - p[1].x) ** 2 + (p[2].y - p[1].y) ** 2)
length += math.sqrt((p[3].x - p[2].x) ** 2 + (p[3].y - p[2].y) ** 2)

print(length)