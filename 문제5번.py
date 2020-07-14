import random

class Account:
    count_count = 0
    
    def __init__(self, name, balance):
        self.deposit_count = 0  # 입금횟수 초기화
        self.deposit_log = []   # 입금내역
        self.withdraw_log = []  # 출금내역  

        self.bank = "SC은행"
        num1 = str(random.randrange(1,1000))
        num2 = str(random.randrange(1,100))
        num3 = str(random.randrange(1,1000000))


        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
        # 빠뜨린 속성 추가 구현
        # ...  
        # 랜덤하게 개좌번호 생성을 구현
        # ...
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
        print('okay')
        # 예금 히스토리 출력을 구현
  
    def withdraw_history(self):
        print('yes')
    # 출금 히스토리 출력을 구현



