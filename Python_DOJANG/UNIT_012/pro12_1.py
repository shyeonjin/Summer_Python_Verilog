# 딕셔너리 만들기
lux= {'health':490,'mana':334,'melee':550,"armor":18.72}
print(lux)

# dict로 딕셔너리 만들기
lux1=dict(health=490,mana=334,melee=550,armor=18.72)
print(lux1)

lux2=dict(zip(['health','mana',"melee","armor"],[490,334,550,18.72]))
print(lux2)

lux3=dict([('health',490),('mana',334),("melee",550),("armor",18.72)])
print(lux3)

lux4=dict({'health':490,'mana':334,'melee':550,"armor":18.72})
print(lux4)