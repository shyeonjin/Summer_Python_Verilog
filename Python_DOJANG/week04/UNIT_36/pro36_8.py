# 연습문제: 리스트에 기능 추가하기
class AdvancedList(list):
    def replace(self,old,new):
        while old in self:
            self[self.index(old)]=new

x=AdvancedList([1,2,3,1,2,3,1,2,3])
x.replace(1,100)
print(x)