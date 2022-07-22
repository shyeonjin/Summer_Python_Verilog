# 심사문제: 게임 캐릭터 클래스 만들기
# 입력으로 체력, 마나 ,AP입력
# 애니클래스를 생성, 티버 스킬의 피해량이 출력되도록 만드세요
# 티버의 피해량은 Ap *0.65 +400

class Annie:
    def __init__(self,health,mana,AP):
        self.health=health
        self.mana=mana
        self.AP=AP
    
    def tibbers(self):
        print("티버: 피해량 %.2f"%(self.AP*0.65+400))

first,second,third=map(float,input("능력치를 입력하세요").split())
R=Annie(health=first,mana=second,AP=third)
R.tibbers()