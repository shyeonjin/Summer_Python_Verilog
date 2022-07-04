# 복잡한 도형 그리기
import turtle as t
t.shape('turtle')
t.circle(120)

t.clear()

# 원을 반복해서 그리기
n=60
t.speed("fastest")
for i in range(n):
    t.circle(120)
    t.right(360/n)

t.clear()
# 선으로 복잡한 무늬 그리기
for i in range(300):
    t.forward(i)
    t.right(91)


t.mainloop()