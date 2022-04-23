import pymysql
import DBUser
import DBLog

def printMenual():
    menu = input('''
            ----------------------------
            1. 사용자 수정
            2. 사용자 로그 조회
            3. 작성한 Web Contents 확인
            ----------------------------
            *나가려면 Q를 누르세요*\n''')
    return menu

def choiceMenu(userID, userPWD):
    ID = userID
    PWD = userPWD

    print("사용자 페이지입니다.")
    while True:
        menu = printMenual()

        if menu == '1':
            # 사용자 수정 선택
            print("수정할 항목을 선택해주세요.")
            subMenu = input('''
                --------------------
                1. Password
                2. Name
                --------------------
                *나가려면 Q를 누르세요*\n''')
            if subMenu == '1':
                edit = input("수정할 Password를 입력해주세요: ")
            elif subMenu == '2':
                edit = input("수정할 Name을 입력해주세요: ")
            elif subMenu == 'q':
                return ''
            
            # DBUser.updateUser() 호출
            res = DBUser.updateUser(subMenu, edit, ID, PWD)
            return res
        elif menu == '2':
            # 사용자 로그 조회 선택
            print("사용자 로그를 조회합니다.")
            key = input("*로그를 새로고침 하려면 R, 나가려면 Q를 누르세요*\n")
            if key == 'q':
                return ''
            elif key == 'r':
                # 동섭님 refresh 함수 호출
                print("새로고침")
                return ''
            else:
                # DBLog.selectLog() 호출
                res = DBLog.selectLog(ID)
                return res
        elif menu == '3':
            # 작성한 Web Contents 확인 선택
            print("작성한 Web Contents 확인\n")
            return ''
        elif menu == 'q':
            return ''
        else:
            print("잘못된 입력값입니다. 다시 입력해주세요.")
            continue

def printResult(result):
    if result == '':
        print("종료되었습니다.\n")
    elif not result:
        print("변경되었습니다.\n")
    else:
        for i in result:
            print(i)
        print("")