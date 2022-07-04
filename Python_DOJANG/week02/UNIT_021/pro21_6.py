# 심사문제: 별 그리기
# 표준입력으로 꼭짓점 개수와 선의 길이 입력
# 꼭짓점(범위 5~10), 선의 길이(50~150)
# 시계방향으로 출력
import turtle as t
t.shape("turtle")

n,length=map(int,input("꼭짓점과 길이 입력:").split())
for i in range(n):
    t.fd(length)
    t.rt((360/n)*2)
    t.fd(length)
    t.lt(360/n)

t.mainloop()

