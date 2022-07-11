# 연습문제: 이미지 파일만 가져오기
# 확장자가 .jpg, .png인 이미지 파일을 출력
# 람다 표현식에서 확장자를 검사할 때 문자열 메서드를 활용
files=['font','1.png','10.jpg','11.gif','2.jpg','3png','table.xclx','spec.docx']

print(list(filter(lambda x:x.find('.jpg') !=-1 or x.find('.png') !=-1,files)))