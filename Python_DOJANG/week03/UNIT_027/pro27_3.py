# 파이썬 객체를 파일에 저장하기, 가져오기

# 파이썬 객체를 파일에 저장하기

from audioop import add
import pickle

name='james'
age=17
address= '서울시 서초구 반포동'
scores={'korean':90,'english':95,'mathematics':84,'science':82}

with open('james.p','wb') as file:
    pickle.dump(name,file)
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(scores,file)

# 파일에서 파이썬 객체 읽기
with open('james.p','rb') as file:
    name=pickle.load(file)
    age=pickle.load(file)
    address=pickle.load(file)
    scores=pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)