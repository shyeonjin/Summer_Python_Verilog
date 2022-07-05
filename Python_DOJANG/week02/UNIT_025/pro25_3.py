# 딕셔너리 표현식 사용하기
keys=["a","b","c","d"]
x={key:value for key,value in dict.fromkeys(keys).items()}
print(x)

print({key:0 for key in dict.fromkeys(['a','b','c','d']).keys()})
print({value:0 for value in {"a":10,"b":20,"c":30,"d":40}.values()})

print({value:key for key,value in {"a":10,"b":20,"c":30,"d":40}.items()})

# 딕셔너리 표현식에서 if 조건문 사용하기
#x={'a':10, 'b':20,'c':30,'d':40}
#for key,value in x.items():
#    if value==20:
#        del x[key]
#print(x)

x={'a':10, 'b':20,'c':30,'d':40}
x={key:value for key,value in x.items() if value !=20}
print(x)