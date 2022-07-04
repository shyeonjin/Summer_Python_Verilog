# 다각형 그리기
# for문 사용 사각형 그리기
import turtle as t
t.shape('turtle')


for i in range(4):
    t.forward(100)
    t.right(90)

t.clear()

# 오각형 그리기
for i in range(5):
    t.forward(100)
    t.right(360/5)


t.clear()

# 다각형그리기
n=int(input())
for i in range(n):
    t.forward(100)
    t.right(360/n)


t.clear()

# 다각형에 색칠하기
n=6
t.color("red")
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(360/n)
t.end_fill()

t.mainloop()


