class Bank:
   def open_account(self):
      print("새로운 계좌가 생성되었습니다.")

   def deposit(blance, money) :
      print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
      return balance + money
   
   def withdraw(balance, money):
      if balance >= money:
         print("{0}원 출금이 완료되었습니다. 잔액은 {1}원입니다. ".format(money, balance - money))
      else :
         print("잔액이 부족합니다. 잔액은 {0}원 입니다.".format(balance))

balance = 10000

while True :
   print("""
   1. 입금
   2. 출금
   3. 잔액확인
   4. 종료
   """)
   a = int(input("상품을 골라주세요 :"))

   if a == 1:
      money = int(input("얼마를 입금하시겠습니까? : "))
      Bank.deposit(balance, money)
      balance = balance + money
      # balance = deposit(balance, money)

   elif a == 2:
      money = int(input("얼마를 출금하시겠습니까? : "))
      Bank.withdraw(balance, money)
      balance = balance - money

   elif a == 3:
      print("현재 잔액은 {0}원 입니다.".format(balance))
   
   elif a == 4:
      break

   else :
      print("다시 입력해주십시오")