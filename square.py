# class square:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#         print(width * height)

# a = square(4, 5)



# class animal:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
        

# class cat(animal):
#     print("고양이 울음소리는 야옹")
#     print("이름: ", name, "종: ", kind)

# class dog(animal):
#     print("강아지 울음소리는 왈왈")
#     print("이름: ", name, "종: ", kind)

# class mouse(animal):
#     print("쥐 소리는 찍찍")
#     print("이름: ", name, "종: ", kind)


# dog = dog('멍멍이', '개')

# cat = cat('야옹이', '고양이')

# mouse = mouse('찍찍이', '쥐')




## 강사님 풀이

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height ## self 꼭 들어가야함
    def perimeter(self):
        return (self.width + self.height) * 2

rec = Rectangle(2,3)
print(rec.area()) ##함수이기 떄문에 () 꼭 붙여야 함)



class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Dog(Animal):
    def bark(self):
        return '왈왈'

class Cat(Animal):
    def meow(self):
        return '야옹'

animal = Animal('name', 2)
dog1 = Dog('강아지', 5)
print(animal.Dog())


## global

av = 5

def a() :
    global av
    av = av + 5 
    ## av = av + 5 ## 이때부터 av는 지역변수가 되버림
    print(av)
