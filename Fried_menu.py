""" - 돈까스집으로 하고 돈까스 종류를 고르면 토핑 종류를 고르기
- 주문, 초기화, 전체 출력 기능
- 상세한 부분은 추가 하지 않음
- Java로 구현해볼 것.
- GitHub Desktop 실험중
"""
import sys

class fried:
    def __init__(self):
        self.menu_list1 = ["등심 돈까스", 0]
        self.menu_list2 = ["치즈 돈까스", 0]
        self.menu_list3 = ["고구마 돈까스", 0]
        self.menu_list4 = ["고구마 치즈 돈까스", 0]
        self.menu_list5 = ["등심 고구마 치즈 돈까스", 0]
        self.menu()

    def menu(self):#메뉴
        print("\n\n")

        print(" 1. 주문하기")     
        print(" 2. 주문 초기화하기")
        print(" 3. 주문 확인하기")
        print(" 4. 프로그램 종료")
        
        self.menu_num = int(input(" 메뉴를 선택해주십시오 : "))

        if self.menu_num == 1:#주문하기
            self.menu_Add()

        elif self.menu_num == 2:#주문 초기화
            self.menu_Reset()

        elif self.menu_num == 3:#주문 확인
            self.menu_Output()
        
        elif self.menu_num == 4:#프로그램 종료
            sys.exit()

        else :
            print("숫자를 잘못 입력하셨습니다. 다시 입력해 주십시오. ")
            self.menu()

    def menu_Add(self):#주문하기 clear
        print("\n")
        print(" 1. 등심 돈까스")
        print(" 2. 치즈 돈까스")
        print(" 3. 고구마 돈까스")
        print(" 4. 고구마 치즈 돈까스")
        print(" 5. 등심 고구마 치즈 돈까스")
        print(" 메뉴를 선택해주십시오 : ")

        self.menu_get = int(input())

        if self.menu_get == 1:
            print("등심 돈까스를 선택하셨습니다. \n")
            menu_dd = int(input("수량을 입력하세요 : "))
            print("등심 돈까스 {0}개 선택하셨습니다. ".format(menu_dd))
            self.menu_list1[1] += menu_dd
            self.menu()

        elif self.menu_get == 2:
            print("치즈 돈까스를 선택하셨습니다. \n")
            menu_dd = int(input("수량을 입력하세요 : "))
            print("치즈 돈까스 {0}개 선택하셨습니다. ".format(menu_dd))
            self.menu_list2[1] += menu_dd
            self.menu()

        elif self.menu_get == 3:
            print("고구마 돈까스를 선택하셨습니다. \n")
            menu_dd = int(input("수량을 입력하세요 : "))
            print("고구마 돈까스 {0}개 선택하셨습니다. ".format(menu_dd))
            self.menu_list3[1] += menu_dd
            self.menu()

        elif self.menu_get == 4:
            print("고구마 치즈 돈까스를 선택하셨습니다. \n")
            menu_dd = int(input("수량을 입력하세요 : "))
            print("고구마 치즈 돈까스 {0}개 선택하셨습니다. ".format(menu_dd))
            self.menu_list4[1] += menu_dd
            self.menu()

        elif self.menu_get == 5:
            print("등심 고구마 치즈 돈까스를 선택하셨습니다. \n")
            menu_dd = int(input("수량을 입력하세요 : "))
            print("등심 고구마 치즈 돈까스 {0}개 선택하셨습니다. ".format(menu_dd))
            self.menu_list5[1] += menu_dd
            self.menu()

        else :
            print("\n")
            print("잘못된 숫자를 입력하셨습니다. 다시 입력해주세요 ")
            self.menu()

    def menu_Reset(self):#주문 초기화 clear
        self.menu_list1 = ["등심 돈까스", 0]
        self.menu_list2 = ["치즈 돈까스", 0]
        self.menu_list3 = ["고구마 돈까스", 0]
        self.menu_list4 = ["고구마 치즈 돈까스", 0]
        self.menu_list5 = ["등심 고구마 치즈 돈까스", 0]

        self.menu()

    def menu_Output(self):#주문 확인
        if self.menu_list1[1] != 0:
            print(self.menu_list1)

        if self.menu_list2[1] != 0:
            print(self.menu_list2)

        if self.menu_list3[1] != 0:
            print(self.menu_list3)

        if self.menu_list4[1] != 0:
            print(self.menu_list4)

        if self.menu_list5[1] != 0:
            print(self.menu_list5)

        self.menu()
    

fucking_fried = fried()