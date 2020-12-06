import random # 랜덤모듈


class Account: # 클래스 변수 생성
    # class variable
    account_count = 0 #계좌갯수의 초기값

    def __init__(self, name, balance):
        self.deposit_count = 0 # 입금횟수의 초기값
        self.deposit_log = [] # 입금기록 리스트
        self.withdraw_log = [] # 출금기록 리스트

        self.name = name #객체인자를 생성하여 클래스의 name을 바인딩
        self.balance = balance #객체인자를 생성하여 클래스의 balance를 바인딩
        self.bank = "SC은행" #객체인자를 생성하여 클래스의 bank를 바인딩

        # 3-2-6
        num1 = random.randint(0, 999) # 0 <= i <= 999의 범위에서 랜덤한 수
        num2 = random.randint(0, 99) # 0 <= i <= 99
        num3 = random.randint(0, 999999) # 0 <= i <= 999999

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001' 입력한 자리수로 확장
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 계좌번호 (001-01-000001)
        Account.account_count += 1 # 계좌가 생성될 때마다 1씩 증가

    @classmethod #객체에 접근할 필요가 없는 메서드
    def get_account_num(cls): #계좌를 출력하는 메서드 cls을 입력함으로서 클래스의 이름이 넘어옴
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount): # 계좌입금을 위한 메서드
        if amount >= 1: # 1원 이상 입금
            self.deposit_log.append(amount) # 입금내역기록
            self.balance += amount # amount만큼 잔고에 더함

            self.deposit_count += 1 # 입금횟수가 추가됨
            if self.deposit_count % 5 == 0:    # 5의 배수이면
                # 이자 지급
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount): # 계과출금을 위한 메서드
        if self.balance > amount: # 잔고의 금액이 출금하는 양보다 많을 때 실행
            self.withdraw_log.append(amount) # 출금내역기록
            self.balance -= amount  # amount만큼 잔고에서 뺌

    def display_info(self): # 계좌정보출력 메서드
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self): # 출금내역출력 메서드
        for amount in self.withdraw_log: # 출금기록에서 기록된 amount를 출력
            print(amount)

    def deposit_history(self): # 입금내역출력 메서드
        for amount in self.deposit_log: # 입금기록에서 기록된 amount를 출력
            print(amount)


k = Account("Kim", 1000) # Kim의 클래스 생성
k.deposit(100) #입금
k.deposit(200)
k.deposit(300)
k.deposit_history() #입금내역확인

k.withdraw(100) #출금
k.withdraw(200)
k.withdraw_history() #출금내역확인