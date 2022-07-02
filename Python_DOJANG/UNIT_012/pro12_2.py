# 딕셔너리의 키에 값 할당
lux= {'health':490,'mana':334,'melee':550,"armor":18.72}
lux['health']=2037
lux['mana']=1184
print(lux)

lux['mana_regen']=3.28
print(lux)

# 딕셔너리에 키가 있는지 확인
lux= {'health':490,'mana':334,'melee':550,"armor":18.72}
print('health' in lux)
print("attack_speed" in lux)
print('health' not in lux)
print("attack_speed" not in lux)

# 딕셔너리의 키 개수 구하기
lux= {'health':490,'mana':334,'melee':550,"armor":18.72}
print(len(lux))
print(len({'health':490,'mana':334,'melee':550,"armor":18.72}))

