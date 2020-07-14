# 트럼프 카드 52장(조커 제외)을 1~52의 정수로 출력하는 프로그램을 작성해 보세요.

# 다음과 같은 조건을 참고합니다.

# 1~13 : 스페이드 A ~ K로 저장
# 14~26 : 하트 A ~ K 로 저장
# 27~39: 다이아몬드 A ~ K로 저장
# 40~52: 크로버 A ~ K로 저장
# 조건문(if, elif, else) 과 반복문(for)을 활용하여

# 출력 예시와 같이 출력하는 코드를 작성하여 실행하시오.

## 카드 순서 : A 2 3 4 5 6 7 8 9 10 J Q K

## A ~ K 까지 적는 알고리즘
# for i in range(13):
#     if i == 0:
#         print("A")
#     elif i > 0 and i == 9:
#         print(i)
#     elif i == 10:
#         print("J")
#     elif i == 11:
#         print("Q")
#     else:
#         print("K")

## 스페이드 ~ 클로버 적는 알고리즘
# for i in range(4):
#     if i == 0:
#         for j in range(1, 14):
#             if j == 1:
#                 print("Spade A")
#             elif 1 < j <= 10:
#                 print("Spade", j)
#             elif j == 11:
#                 print("Spade J")
#             elif j == 12:
#                 print("Spade Q")
#             else:
#                 print("Spade K")
        
#     elif i == 1:
#         for j in range(1, 14):
#             if j == 1:
#                 print("Heart A")
#             elif 1 < j <= 10:
#                 print("Heart", j)
#             elif j == 11:
#                 print("Heart J")
#             elif j == 12:
#                 print("Heart Q")
#             else:
#                 print("Heart K")
#     elif i == 2 :
#         for j in range(1, 14):
#             if j == 1:
#                 print("Diamond A")
#             elif 1 < j <= 10:
#                 print("Diamond", j)
#             elif j == 11:
#                 print("Diamond J")
#             elif j == 12:
#                 print("Diamond Q")
#             else:
#                 print("Diamond K")
#     else:
#         for j in range(1, 14):
#             if j == 1:
#                 print("Clover A")
#             elif 1 < j <= 10:
#                 print("Clover", j)
#             elif j == 11:
#                 print("Clover J")
#             elif j == 12:
#                 print("Clover Q")
#             else:
#                 print("Clover K")



#  2. 파이썬 피보나치 수열 [이재화]
# 피보나치 수열은

# 0항을 0, 1항을 1로 두고 2항부터는

# 바로 전의 숫자 2개를 더한 값을 출력하는 처리를 반복실행하는 계산입니다.

# 이러한 피보나치 수열을 계산하는

# 조건문(if, elif, else)이 들어간 함수를 작성하고, 반복문(for)을 통해 출력하시오.

# 다음과 같은 조건을 참고합니다. (채점기준)

# 처음 여섯 항은 각각 1, 1, 2, 3, 5, 8이다
# 총 8개의 항을 출력하여 주세요.
# 조건문은 한번 이상 활용해 주세요.


# first_num = 0
# second_num = 1
# sum = 0

# # for i in range(8):
# #     if i == 0:
# #         print(second_num)
# #     else:
# #         sum = first_num + second_num
# #         first_num = second_num
# #         second_num = sum
# #         print(sum)



    
# # 3. 백종원 씨는 너무 많은 프랜차이즈 정보를 확인하는 것에 지쳐서,

# # csv 파일을 통해 원하는 데이터를 읽고, 추가할 수 있는 시스템을 맡기기로 결정하였다.

# # 광주인공지능사관학교 학생들이 파이썬 실력이 훌륭하다는 말을 듣고, 찾아와 당신에게 의뢰하였다.

# # 주석에 지시에 따라 함수를 완성하고 실행하시오

# baeks = [
#     {
#         "name" : "빽다방 종로관철점" ,
#         "location" : "서울 종로구 종로10길 21",
#         "goods" : "커피",
#         "num" : "00-2445-5324"
#     },
#     {
#         "name" : "백인공지능 판매점" ,
#         "location" : "광주 북구 첨단과기로",
#         "goods" : "인공지능",
#         "num" : "1234-5678-9123"
#     },
#     {
#         "name" : "백인공지능 판매점" ,
#         "location" : "광주 북구 첨단과기로",
#         "goods" : "인공지능",
#         "num" : "1234-5678-9123"
#     },
#     {
#         "name" : "백인공지능 판매점" ,
#         "location" : "광주 북구 첨단과기로",
#         "goods" : "인공지능",
#         "num" : "1234-5678-9123"
#     }
# ]

# import csv

# def main() :
#     selected = input("1 - 상점추가, 2 - 상점 모두 보기, 3 - 상점 위치 찾기, 4 - 판매하는 상품 종 류 보기, 5 - 상점 전화번호 찾기, 0 - 프로그램 종료")

#     # TODO 0. csv 파일이 생성되지 않으면 읽을 수 없습니다. TODO 1의 등록하는 기능을 구현하여, 예시 데이터를 Write 하는 과정을 먼저 수행해주세요.
    
#     if selected == '1' :
#         with open('baeks.csv', 'w', encoding='utf-8', newline='') as f:
#             csvw = csv.DictWriter(f, fieldnames=['name', 'location', 'goods', 'num'])
#             csvw.writeheader()
#             csvw.writerows(baeks)
#             print("상점추가가 완료되었습니다.")
                
#     # TODO 1. 상점의 데이터를 csv 파일에 등록하는 기능
#     # - 상점의 이름, 위치, 상품종류, 전화번호를 예시 데이터에 맞게 입력을 받기
#     # - 입력 받은 데이터를 csv 파일에 write
#     elif selected == '2' :
#         with open('baeks.csv', 'r', encoding='utf-8') as csvfile:
#             csvr = csv.DictReader(csvfile)
#             for i in csvr:
#                 print(i['name'])

#     # TODO 2. 상점의 
#     # 이름을 모두 출력하는 기능
#     # - csv 에 등록되어 있는 모든 파일의 이름을 출력하기
#     elif selected == '3' :
#         with open('baeks.csv', 'r', encoding='utf-8') as csvfile:
#             csvr = csv.DictReader(csvfile)
#             x = input("이름 입력 : ")
#             count = 0
#             if count == 0:
#                 for i in csvr:
#                     if x == i['name']:
#                         print(i['location'])
                    
                        
 
#     # TODO 3. 상점 위치 찾기 기능
#     # - 상점 이름을 입력받고, 해당 상점의 위치를 출력 해주기
#     elif selected == '4' :
#         with open('baeks.csv', 'r', encoding='utf-8') as csvfile:
#             csvr = csv.DictReader(csvfile)
#             x = input("이름 입력 : ")
#             count = 0
#             if count == 0:
#                 for i in csvr:
#                     if x == i['name']:
#                         print(i['goods'])

        
#     # TODO 4. 판매하는 물건 보기
#     # - 상점 이름을 입력받고, 해당 상점의 판매하는 상품 종류 출력 해주기
#     elif selected == '5' :
#         with open('baeks.csv', 'r', encoding='utf-8') as csvfile:
#             csvr = csv.DictReader(csvfile)
#             x = input("이름 입력 : ")
#             count = 0
#             if count == 0:
#                 for i in csvr:
#                     if x == i['name']:
#                         print(i['num'])
#     # TODO 5. 상점 전화번호 찾기
#     # - 상점 이름을 입력받고, 해당 상점의 전화번호를 출력하는 기능
#     elif selected == '0' :
#         print("종료합니다")
#     exit()
 
# # 메인 함수 실행
# main()



import random

class Account:
  # 클래스 변수
  account_count = 0

  def __init__(self, name, balance):
    self.deposit_count = 0  # 입금횟수 초기화
    self.deposit_log = []   # 입금내역
    self.withdraw_log = []  # 출금내역

    # 빠뜨린 속성 추가 구현
    # ...
    self.bank = "SC은행"
    num1 = random.randrange(1,1000)
    num2 = random.randrange(1,100)
    num3 = random.randrange(1,1000000)
    # 랜덤하게 개좌번호 생성을 구현
    # ...

    self.account_number = num1 + '-' + num2 + '-' + num3
    Account.account_count += 1
  
  @classmethod
  def get_account_num(cls):
    print(cls.account_count)
  
  def deposit(self, amount):
    if amount > 1:
      self.deposit_log.append(amount)
      self.balance += amount

      self.deposit_count += 1
      if self.deposit_count % 5 == 0:   # 5, 10, 15 ...
        self.balance *= 1.01            # 이자
    
  def withdraw(self, amount):
    if self.balance > amount:
      self.withdraw_log.append(amount)
      self.balance -= amount
    
  def display_info(self):
      print("은행이름:", self.bank)
      print("예금주:", self.name)
      print("계좌번호:", self.account_number)
      print("잔고:", self.balance)
    # 정보출력을 구현
    # ...
  
  def deposit_history(self):
      for i in deposit_log:
          print(i)
    # 예금 히스토리 출력을 구현
  
  def withdraw_history(self):
      for i in self.withdraw_log:
          print(i)


    # 출금 히스토리 출력을 구현



kim = Account("김민수", 100)
print("은행이름:", kim.bank) 
print("계좌번호:", kim.account_number) 
print('-'*20)

kim = Account("김민수", 100)
print("총 계좌수:", Account.account_count)
lee = Account("이민수", 100)
print("총 계좌수:", Account.account_count)
print('-'*20)

kim = Account("김민수", 100)
lee = Account("이민수", 100)
Account.get_account_num()
print('-'*20)

kim = Account("김민수", 100)
kim.deposit(1)
print(kim.balance)
kim.deposit(100)
print(kim.balance)
print('-'*20)

p = Account("파이썬", 10000)
p.display_info()
print('-'*20)

kim = Account("김민수", 100)
kim.deposit(100)
kim.withdraw(90)
print(kim.balance)
print('-'*20)

p = Account("파이썬", 10000)
p.deposit(100)
p.deposit(200)
p.deposit(300)
p.deposit_history()
print('-'*20)

p.withdraw(100)
p.withdraw(200)
p.withdraw_history()
print('-'*20)