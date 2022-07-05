# 딕셔너리의 할당과 복사
x={'a':0,'b':0,'c':0,'d':0}
y=x
print(x is y)
y['a']=90
print(y,x)

x={'a':0,'b':0,'c':0,'d':0}
y=x.copy()
print(x is y)
print(x==y)
y['a']=90
print(y,x)

# 중첩 딕셔너리의 할당과 복사 알아보기
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y=x.copy()
print(y)

y['a']['python'] = '2.7.15'
print(x,y)

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy

y=copy.deepcopy(x)
y['a']['python'] = '2.7.15'
print(x,y)
