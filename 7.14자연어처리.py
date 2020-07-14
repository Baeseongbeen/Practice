import re ##(Regular Expression) 정규 표현식

a = '김준태 - 학점 2.0' ## 순서 바꾸고 싶을 떄
b = 'ab123 abcdefg a'
p = re.compile('a')
matched = p.match(b) ## match 함수
searched = p.search(b)
print(matched)
print(searched)

p = re.compile(r'(?P<name>\w+)\s.\s+(?P<grade>.+\s.+)')## 김준태는 name 그룹으로, 학점 2.0 은 grade 그룹으로 지정됨

print(p.match(a).group(2)) ## group(2) :: 두번째 매칭한 그룹이 나오게 됨
print(p.sub("\g<grade> - ")) 

a = '123512341234'

p = re.compile(r'\d+') # +의 역활 : \d\d\d\d\d\d ... 의미
# .+ : ........~~ 의미하겠지