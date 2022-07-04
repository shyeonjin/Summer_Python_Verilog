# 연습문제: 오각별 그리기
# 각 변의 길이 100
# 별의 꼭짓점은 75도를 두 번 회전해서 144도 회전
# 별의 다음 꼭짓점을 그릴 때는 72도 회전  
import turtle as t
t.shape("turtle")
n=5
for i in range(n):
    t.forward(100)
    t.right((360/n)*2)
    t.forward(100)
    t.left(360/n)
t.mainloop()