print("hello")
print("My Repository")
a = 2 **8
print(a)

print('%5d' %a)

b= f'광주인공지능사관학교 학생 수는 {a}'

print(b)

mine = {'name' : 'seongbeen', 'age' : 26, 'phone' : "010-xxxx-xxxx", 'hobby' : 'game'}

print(mine.keys())

c = [1,2,3]
for i in c:
    print(i)
    if i == 2:
        pass ##????
    print('굳굳')

class Pet:
    def __init__(self, name, age):
        self.name = name ##자기 자신의 name은 사용자가 입력한 name
        self.age = age 
        print('펫 등록 완료!')
    def eat(self, food):
        print(f'{food}를 먹습니다')
        
dog = Pet('강아지', 3) ##대소문자 구별
print(dog.name, ",", dog.age)


dog.eat('밥')
