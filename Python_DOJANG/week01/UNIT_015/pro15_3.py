# 연습문제: if,elif,else 모두 사용
# x가 11과 20사이면 '11~20',21과 30사이면 '21~30'해당안하면 '해당없음'
x=int(input())
if 11<=x<=20:
    print("11~20")
elif 21<=x<=30:
    print("21~30")
else:
    print("해당없음")