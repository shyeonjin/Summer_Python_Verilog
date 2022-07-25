# 두 점 사이의 거리 구하기
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
p1 = Point2D(x=30, y=20)    
p2 = Point2D(x=60, y=50)    
 
print('p1: {} {}'.format(p1.x, p1.y))    
print('p2: {} {}'.format(p2.x, p2.y)) 


a = p2.x - p1.x    
b = p2.y - p1.y   
import math
c = math.sqrt((a * a) + (b * b))    
print(c)  


# 절대값 함수
# abs(값) : 정수는 절댓값을 정수로 변환, 실수는 절댓값을 실수로 변환

# math.fabs(값) : 절댓값을 실수로 변환



